from application import app
from flask import render_template, request
import requests
import random

@app.route('/', methods=['GET'])
def home():
    allinfo = requests.get('http://currpair:5003/randompair')
    allinfo = allinfo.text
    allinfolist = allinfo.split(":")
    return render_template('index.html', allinfo = allinfolist, title = 'Home')
