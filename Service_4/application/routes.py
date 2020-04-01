from application import app
from flask import render_template, request
import requests
import ast
import os

secretkey = os.environ.get("secretkey")
secretkey = str(secretkey)


@app.route('/randompair', methods=['GET'])
def sentence():
    region = request.args.get("region")
    mode = request.args.get("mode")
    
    fiatfull = requests.get('http://localhost:5001/randomfiat?region={0}'.format(region)) ##fiatgen (s2)
    crypfull = requests.get('http://localhost:5002/randomcryp') ##crypgen (s3)
    fiatfull = fiatfull.text
    crypfull = crypfull.text

    fiatlist = fiatfull.split(":")
    fiatabv = fiatlist[0]
    print(fiatabv)

    cryplist = crypfull.split(":")
    crypabv = cryplist[0]
    print(crypabv)


    
    if mode == '1':
        val_from = crypabv
        val_to = fiatabv
        abvpair = crypfull + fiatfull
    else:
        val_from = fiatabv
        val_to = crypabv
        abvpair = fiatfull + crypfull

    baseurl = "https://min-api.cryptocompare.com/data/price?"
    endurl = "fsym="+val_from+"&tsyms="+val_to
    apikey = "&api_key="
    url = baseurl+endurl+apikey+secretkey
    print(url)
    
    currency = requests.get(url)
    currency = currency.text
    currency = ast.literal_eval(currency)
    dictlist =[]
    for key, value in currency.items():
        dictlist.append(value)
    value = dictlist[0]

    fullpair = abvpair + str(value)
    print(fullpair)

    return fullpair