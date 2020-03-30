from application import app
import requests
import ast
import os

secretkey = os.environ.get("secretkey")
secretkey = str(secretkey)


@app.route('/randompair', methods=['GET'])
def sentence():
    fiatfull = requests.get('http://fiatgen:5001/randomfiat')
    crypfull = requests.get('http://crypgen:5002/randomcryp')
    fiatfull = fiatfull.text
    crypfull = crypfull.text

    fiatlist = fiatfull.split(":")
    fiatabv = fiatlist[0]
    print(fiatabv)

    cryplist = crypfull.split(":")
    crypabv = cryplist[0]
    print(crypabv)

    baseurl = "https://min-api.cryptocompare.com/data/price?"
    endurl = "fsym="+crypabv+"&tsyms="+fiatabv
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

    fullpair = crypfull + fiatfull + str(value)
    print(fullpair)

    return fullpair