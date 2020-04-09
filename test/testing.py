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

def test_mainurl():
    http = urllib3.PoolManager() 
    r = http.request('GET', 'http://localhost:80/') # can use post method too ## or ip address of the website:5000 when its running on another machine
    assert 200 == r.status  #200 = successful connection

#### Testing Access to the 4 Services aren't available ####

def test_service1():
    http = urllib3.PoolManager() 
    r = http.request('GET', 'http://localhost:5000/') 
    assert r.status != 200  #200 = successful connection (So testing for unsuccessful connection)

def test_service2():
    http = urllib3.PoolManager() 
    r = http.request('GET', 'http://localhost:5001/') 
    assert r.status != 200  #200 = successful connection (So testing for unsuccessful connection)

def test_service3():
    http = urllib3.PoolManager() 
    r = http.request('GET', 'http://localhost:5002/') 
    assert r.status != 200  #200 = successful connection (So testing for unsuccessful connection)

def test_service4():
    http = urllib3.PoolManager() 
    r = http.request('GET', 'http://localhost:5003/') 
    assert r.status != 200  #200 = successful connection (So testing for unsuccessful connection)