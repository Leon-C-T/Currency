from application import app
from flask import render_template, request
from flask_mysqldb import MySQL
import requests
import random
import os

app.config['MYSQL_HOST'] = os.environ.get('MYSQLHOST') #-ip address of SQL DB - environ variable: MYSQLHOST="ip address"
app.config['MYSQL_USER'] = os.environ.get('MYSQLUSER') #-Username for DB - environ variable: MYSQLUSER="root"
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQLPASSWORD') #Password for DB - environ variable: MYSQLPASSWORD="whatever the password is"
app.config['MYSQL_DB'] = os.environ.get('MYSQLDB') #Database thats being used - environ variable: MYSQLDB="whatever database you want to use"

mysql = MySQL(app)
region = 1
mode = 1


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

    global region
    global mode

    region = region
    mode = mode

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
            if reg == '0':
                region = region
            else: 
                region = reg   
            if mod == '0':
                mode = mode
            else:
                mode = mod

        if request.form['action'] == 'random':  
            region = 1    
            mode = random.randrange(1,3,1)
            print(mode)                                                                                                                                                                                                                                                                                          
   
    allinfo = requests.get('http://localhost:5003/randompair?region={0}&mode={1}'.format(region,mode)) ##currpair (s4)
    allinfo = allinfo.text
    allinfolist = allinfo.split(":")
    crypabv = allinfolist[0]
    fiatabv = allinfolist[2]
    price = allinfolist[4]  



    region = int(region)
    reg_op = regiondict.get(region)

    mode = int(mode)
    mode_op = modedict.get(mode)

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


   
    print(regiondict.get(region))
    print(modedict.get(mode))

    return render_template('index.html', allinfo = allinfolist, reg_op = reg_op, mode_op = mode_op, fiat_cryp = fiat_cryp, cryp_fiat = cryp_fiat, title = 'Home')
