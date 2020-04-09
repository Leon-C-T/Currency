from flask import Flask
from flask_mysqldb import MySQL
import os
import urllib3
import time
import pytest

app = Flask(__name__)

app.config['MYSQL_HOST'] = os.environ.get('MYSQLHOST') #-ip address of SQL DB - environ variable: MYSQLHOST="ip address"
app.config['MYSQL_USER'] = os.environ.get('MYSQLUSER') #-Username for DB - environ variable: MYSQLUSER="root"
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQLPASSWORD') #Password for DB - environ variable: MYSQLPASSWORD="whatever the password is"
app.config['MYSQL_DB'] = os.environ.get('MYSQLDB') #Database thats being used - environ variable: MYSQLDB="whatever database you want to use"
app.secret_key = os.environ.get('MYSQLSECRETKEY') # Secret Key for use with session

mysql = MySQL(app)


############################################## URL Test ##############################################

def test_mainurl():
    http = urllib3.PoolManager() 
    r = http.request('GET', 'http://localhost:80/') # can use post method too ## or ip address of the website:5000 when its running on another machine
    assert 200 == r.status  #200 = successful connection

############################################## Database Testing Loop ##############################################



################# Cryp2Fiat Table Testing Loop #################


#### Global Test Vars ####

pytest.testfiatold = "testfiat"
pytest.testcrypold = "testcryp"
pytest.testpriceold = 1010.0101
pytest.idold = "0"
pytest.cur_idnew = "0"



def test_create():

    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM cryp2fiat ORDER BY Cur_ID DESC LIMIT 1")
        mysql.connection.commit()                                                                                                                   
        cur_id = cur.fetchall()                                                                                                                                                              
        cur_idold = cur_id[0]                                                                                                                                                                    
        cur_idold = cur_idold[0]
        pytest.idold = cur_idold
        cur = mysql.connection.cursor()                                                                                                                                                     
        cur.execute("INSERT INTO cryp2fiat (Fiatname, Crypname, Price) VALUES (%s, %s, %s)", (pytest.testfiatold, pytest.testcrypold, pytest.testpriceold))      
        mysql.connection.commit()                                                                                                                                                          
        cur.execute("SELECT * FROM cryp2fiat ORDER BY Cur_ID DESC LIMIT 1")                                                                                                              
        cur_id2 = cur.fetchall()                                                                                                                                                              
        cur_idnew = cur_id2[0]                                                                                                                                                                    
        pytest.cur_idnew = cur_idnew[0]                                                                                                                                                                                                                                                                                                                          
        cur.close()
        assert 1 == (pytest.cur_idnew - cur_idold)

def test_read():

    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM cryp2fiat ORDER BY Cur_ID DESC LIMIT 1")    
        info = cur.fetchall()
        infolist = []
        for i in info:
            for j in i:
                infolist.append(j)
        cur_id = infolist[0]
        fiatname = infolist[1]
        crypname = infolist[2]
        price = infolist[3]                                                                                                                                                                                                                                                                                                                                                                                                       
        cur.close()
        
        assert (pytest.testfiatold == fiatname) == True and (pytest.testcrypold == crypname) == True and (float(pytest.testpriceold) == float(price)) == True 

def test_update():

    with app.app_context():

        fiatnew = "NewFiat"
        crypnew = "NewCryp"
        pricenew = 2020.0202

        cur = mysql.connection.cursor()
        cur.execute("UPDATE cryp2fiat SET Fiatname = %s, Crypname = %s, Price = %s WHERE Cur_ID = %s", (fiatnew, crypnew, pricenew, pytest.cur_idnew))
        mysql.connection.commit()
        cur.close()

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM cryp2fiat ORDER BY Cur_ID DESC LIMIT 1")       
        info = cur.fetchall()
        infolist = []
        for i in info:
            for j in i:
                infolist.append(j)
        cur_id = infolist[0]
        fiatname = infolist[1]
        crypname = infolist[2]
        price = infolist[3]                                                                                                                                                                                                                                                                                                                                                                                                       
        cur.close()

        assert (fiatnew == fiatname) == True and (crypnew == crypname) == True and (float(pricenew) == float(price)) == True 

time.sleep(2)

def test_delete():

    with app.app_context():
        cur = mysql.connection.cursor()

        cur.execute("DELETE FROM cryp2fiat WHERE Cur_ID = %s", [pytest.cur_idnew])
        mysql.connection.commit()

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM cryp2fiat ORDER BY Cur_ID DESC LIMIT 1")   
        info = cur.fetchall()   
        infolist = []
        for i in info:
            for j in i:
                infolist.append(j)
        cur_idold = infolist[0]
        
        value = int(cur_idold) - int(pytest.cur_idnew)

        cur.execute("ALTER TABLE cryp2fiat AUTO_INCREMENT = %s", [pytest.idold])
        
        assert -1 == value

################# Fiat2Cryp Table Testing Loop #################


#### Global Test Vars ####

pytest.testfiatold = "testfiat"
pytest.testcrypold = "testcryp"
pytest.testpriceold = 1010.0101
pytest.idold = "0"
pytest.cur_idnew = "0"



def test_create():

    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM fiat2cryp ORDER BY Cur_ID DESC LIMIT 1")
        mysql.connection.commit()                                                                                                                   
        cur_id = cur.fetchall()                                                                                                                                                              
        cur_idold = cur_id[0]                                                                                                                                                                    
        cur_idold = cur_idold[0]
        pytest.idold = cur_idold
        cur = mysql.connection.cursor()                                                                                                                                                     
        cur.execute("INSERT INTO fiat2cryp (Fiatname, Crypname, Price) VALUES (%s, %s, %s)", (pytest.testfiatold, pytest.testcrypold, pytest.testpriceold))      
        mysql.connection.commit()                                                                                                                                                          
        cur.execute("SELECT * FROM fiat2cryp ORDER BY Cur_ID DESC LIMIT 1")                                                                                                              
        cur_id2 = cur.fetchall()                                                                                                                                                              
        cur_idnew = cur_id2[0]                                                                                                                                                                    
        pytest.cur_idnew = cur_idnew[0]                                                                                                                                                                                                                                                                                                                          
        cur.close()
        assert 1 == (pytest.cur_idnew - cur_idold)

def test_read():

    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM fiat2cryp ORDER BY Cur_ID DESC LIMIT 1")    
        info = cur.fetchall()
        infolist = []
        for i in info:
            for j in i:
                infolist.append(j)
        cur_id = infolist[0]
        fiatname = infolist[1]
        crypname = infolist[2]
        price = infolist[3]                                                                                                                                                                                                                                                                                                                                                                                                       
        cur.close()
        
        assert (pytest.testfiatold == fiatname) == True and (pytest.testcrypold == crypname) == True and (float(pytest.testpriceold) == float(price)) == True 

def test_update():

    with app.app_context():

        fiatnew = "NewFiat"
        crypnew = "NewCryp"
        pricenew = 2020.0202

        cur = mysql.connection.cursor()
        cur.execute("UPDATE fiat2cryp SET Fiatname = %s, Crypname = %s, Price = %s WHERE Cur_ID = %s", (fiatnew, crypnew, pricenew, pytest.cur_idnew))
        mysql.connection.commit()
        cur.close()

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM fiat2cryp ORDER BY Cur_ID DESC LIMIT 1")       
        info = cur.fetchall()
        infolist = []
        for i in info:
            for j in i:
                infolist.append(j)
        cur_id = infolist[0]
        fiatname = infolist[1]
        crypname = infolist[2]
        price = infolist[3]                                                                                                                                                                                                                                                                                                                                                                                                       
        cur.close()

        assert (fiatnew == fiatname) == True and (crypnew == crypname) == True and (float(pricenew) == float(price)) == True 

time.sleep(2)

def test_delete():

    with app.app_context():
        cur = mysql.connection.cursor()

        cur.execute("DELETE FROM fiat2cryp WHERE Cur_ID = %s", [pytest.cur_idnew])
        mysql.connection.commit()

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM fiat2cryp ORDER BY Cur_ID DESC LIMIT 1")   
        info = cur.fetchall()   
        infolist = []
        for i in info:
            for j in i:
                infolist.append(j)
        cur_idold = infolist[0]
        
        value = int(cur_idold) - int(pytest.cur_idnew)

        cur.execute("ALTER TABLE fiat2cryp AUTO_INCREMENT = %s", [pytest.idold])
        
        assert -1 == value
