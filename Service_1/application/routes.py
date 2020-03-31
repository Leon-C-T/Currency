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
@app.route('/', methods=['GET'])
def home():
    allinfo = requests.get('http://currpair:5003/randompair')
    allinfo = allinfo.text
    allinfolist = allinfo.split(":")
    
    crypabv = allinfolist[0]
    fiatabv = allinfolist[2]
    price = allinfolist[4]


    cur = mysql.connection.cursor()                                                                                                                                                   
    cur.execute("INSERT INTO currencylist (Fiatname, Crypname, Price) VALUES (%s, %s, %s)", (crypabv, fiatabv, price))                          
    mysql.connection.commit()                                                                                                                                                         
    cur.execute("SELECT Fiatname, Crypname, Price FROM currencylist ORDER BY Cur_id DESC LIMIT 5")                                                                                                             
    prev_ten = cur.fetchall() 
    print(prev_ten)                        
    cryptenabv = prev_ten[0]     
    fiattenabv = prev_ten[1]                                                                                                                                                             
    prices = prev_ten[2]                                                                                                                                                               
    print(cryptenabv)
    print(fiattenabv)
    print(prices)                                                                                                                                                       
    cur.close()                                                                                                                                                                         

    return render_template('index.html', allinfo = allinfolist, prev_ten = prev_ten, title = 'Home')
