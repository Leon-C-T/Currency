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
region = 1
mode = 1
crypx = 1


@app.route('/', methods=['GET','POST']) ##flaskcur (s1)
def home():
    
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

    global region
    global mode
    global crypx

    region = region
    mode = mode
    crypx = crypx

    cur = mysql.connection.cursor()  
    cur.execute("SELECT Crypname, Fiatname, Price FROM cryp2fiat ORDER BY Cur_id DESC LIMIT 5")                                                                                                             
    cryp_fiat = cur.fetchall()
    cur.close()

    cur = mysql.connection.cursor()  
    cur.execute("SELECT Fiatname, Crypname, Price FROM fiat2cryp ORDER BY Cur_id DESC LIMIT 5")                                                                                                             
    fiat_cryp = cur.fetchall()
    cur.close() 

    cryptenabv = cryp_fiat[0]     
    fiattenabv =cryp_fiat[1]                                                                                                                                                             
    prices = cryp_fiat[2]             


    if request.method == "POST":
        if request.form['action'] == 'specified':  
            details = request.form 
            reg = details["region"]
            mod = details["mode"]
            cry = details["crypx"]
            if reg == '0':
                region = region
            else: 
                region = reg   
            if mod == '0':
                mode = mode
            else:
                mode = mod
            if cry == '0':
                crypx = crypx
            else:
                crypx = cry

        if request.form['action'] == 'random':  
            region = 1    
            mode = random.randrange(1,3,1) 
            crypx = random.randrange(1,5,1)                                                                                                                                                                                                                                                                                        
   

    allinfo = requests.get('http://currpair:5003/randompair?region={0}&mode={1}&crypx={2}'.format(region,mode,crypx)) ##currpair (s4)
    allinfo = allinfo.text
    allinfolist = allinfo.split(":")

    crypabv = allinfolist[0]
    fiatabv = allinfolist[2]
    price = allinfolist[4]  


    region = int(region)
    reg_op = regiondict.get(region)

    mode = int(mode)
    mode_op = modedict.get(mode)

    crypx = int(crypx)
    crypx_op = crypxdict.get(crypx)

    if mode == 1:
        cur = mysql.connection.cursor()                                                                                                                                                   
        cur.execute("INSERT INTO cryp2fiat (Fiatname, Crypname, Price) VALUES (%s, %s, %s)", (fiatabv, crypabv, price))                          
        mysql.connection.commit()  
        cur.close()   
    else:
        cur = mysql.connection.cursor()                                                                                                                                                   
        cur.execute("INSERT INTO fiat2cryp (Fiatname, Crypname, Price) VALUES (%s, %s, %s)", (fiatabv, crypabv, price))                          
        mysql.connection.commit()  
        cur.close()   

    return render_template('index.html', allinfo = allinfolist, reg_op = reg_op, mode_op = mode_op, crypx_op = crypx_op, fiat_cryp = fiat_cryp, cryp_fiat = cryp_fiat, title = 'Home')
