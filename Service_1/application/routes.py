from application import app
from flask import render_template, request
from flask_mysqldb import MySQL
import requests
import random
import os

app.config['MYSQL_HOST'] = os.environ.get('MYSQLHOST') #-ip address of SQL DB 
app.config['MYSQL_USER'] = os.environ.get('MYSQLUSER') #-Username for DB 
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQLPASSWORD') #Password for DB 
app.config['MYSQL_DB'] = os.environ.get('MYSQLDB') #Database thats being used 

mysql = MySQL(app)

#### Global URL Variables ####

region = 1
mode = 1
crypx = 1

####################################### Start of App Route for Service 1 (flaskcur) #######################################

@app.route('/', methods=['GET','POST']) 
def home():

##### Dictionaries for Option Selects on index.html #####

    regiondict = {
        0 : "Random Region",
        1 : "Random Region",
        2 : "Europe",
        3 : "Oceania",
        4 : "North America",
        5 : "South America",
        6 : "West and South Asia",
        7 : "North and East Asia",
        8 : "Africa"
    }

    modedict = {
        0 : "Cryp -> Fiat",
        1 : "Cryp -> Fiat",
        2 : "Fiat -> Cryp",
    }

    crypxdict = {
        0 : "From Top 10 Coins",
        1 : "From Top 10 Coins",
        2 : "From Popular 30 Coins",
        3 : "From Top 50 Coins",
        4 : "From Top 100 Coins"
    }

##### Global Variables for Mode Selected #####

    global region
    global mode
    global crypx

    region = region
    mode = mode
    crypx = crypx

##### Read Last 5 Fiat2cryp and cryp2fiat Table Values #####

    cur = mysql.connection.cursor()  
    cur.execute("SELECT Crypname, Fiatname, Price FROM cryp2fiat ORDER BY Cur_id DESC LIMIT 5")                                                                                                             
    cryp_fiat = cur.fetchall()
    cur.close()

    cur = mysql.connection.cursor()  
    cur.execute("SELECT Fiatname, Crypname, Price FROM fiat2cryp ORDER BY Cur_id DESC LIMIT 5")                                                                                                             
    fiat_cryp = cur.fetchall()
    cur.close() 

    #cryptenabv = cryp_fiat[0]     
    #fiattenabv =cryp_fiat[1]                                                                                                                                                             
    #prices = cryp_fiat[2]             

##### If New Pair button or Im Feeling Crypto Button is Clicked: #####

## If New Pair Button is Clicked:

    if request.method == "POST":
        if request.form['action'] == 'specified':  
            details = request.form 
            reg = details["region"]
            mod = details["mode"]
            cry = details["crypx"]
            if reg == '0':             ##### If no change to region
                region = region        # Keeps region the same value as previously
            else:                      # Else Updates region url variable #####
                region = reg            
            if mod == '0':             ##### If no change to mode
                mode = mode            # Keeps mode the same value as previously
            else:                      # Else Updates mode url variable #####
                mode = mod              
            if cry == '0':             ##### If no change to crypto list chosen
                crypx = crypx          # Keeps crypto the same value as previously
            else:                      # Else Updates crypto url variable #####
                crypx = cry             

## If Im Feeling Crypto Button is Clicked:

        if request.form['action'] == 'random':  
            region = 1                          # Sets Region URL Variable (for Service 2) To 1 (for a random fiat currency)
            mode = random.randrange(1,3,1)      # Sets Mode URL Variable (for Service 4) to a Random Value (for a random mode)
            crypx = random.randrange(1,5,1)     # Sets Crypto URL Variable (for Service 3) to a Random Value (for a random crypto list)                                                                                                                                                                                                                                                                                   
   


##### Service 4 Call (currpair) #####

    allinfo = requests.get('http://currpair:5003/randompair?region={0}&mode={1}&crypx={2}'.format(region,mode,crypx)) # Requests information using passed URL Variables for options
    allinfo = allinfo.text  # Extracts text information
    allinfolist = allinfo.split(":") # Splits text information at Colons

    crypabv = allinfolist[0]    ## Crypto Abbreviation
    fiatabv = allinfolist[2]    ## Fiat Abbreviation
    price = allinfolist[4]      ## Price Returned


    region = int(region)            ## Converts Region Value Selected into an Integer
    reg_op = regiondict.get(region) ## Returns Region Text from Dictionary using Region Value

    mode = int(mode)                ## Converts Mode Value Selected into an Integer
    mode_op = modedict.get(mode)    ## Returns Mode Text from Dictionary using Mode Value

    crypx = int(crypx)              ## Converts Crypto List Value Selected into an Integer
    crypx_op = crypxdict.get(crypx) ## Returns Crypto List Text from Dictionary using Crypto List Value

    if mode == 1:                   ## If mode selected is cryp2fiat, Inserts data into cryp2fiat table
        cur = mysql.connection.cursor()                                                                                                                                                   
        cur.execute("INSERT INTO cryp2fiat (Fiatname, Crypname, Price) VALUES (%s, %s, %s)", (fiatabv, crypabv, price))                          
        mysql.connection.commit()  
        cur.close()   
    else:                           ## If mode selected is fiat2cryp, Inserts data into fiat2cryp table
        cur = mysql.connection.cursor()                                                                                                                                                   
        cur.execute("INSERT INTO fiat2cryp (Fiatname, Crypname, Price) VALUES (%s, %s, %s)", (fiatabv, crypabv, price))                          
        mysql.connection.commit()  
        cur.close()   

##### Returns Index.html Page With all relevant information #####

    return render_template('index.html', allinfo = allinfolist, reg_op = reg_op, mode_op = mode_op, crypx_op = crypx_op, fiat_cryp = fiat_cryp, cryp_fiat = cryp_fiat, title = 'Home')
