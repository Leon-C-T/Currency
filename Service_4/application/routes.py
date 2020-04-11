from application import app
from flask import render_template, request
import requests
import ast
import os

## Returns Secret Key for URL External API Call ##
secretkey = os.environ.get("secretkey")
secretkey = str(secretkey)

####################################### Start of App Route for Service 4 (currpair) #######################################

@app.route('/randompair', methods=['GET'])
def sentence():

## Gets URL Variables from Service 1 (As selected by User in Service 1):

    region = request.args.get("region")
    mode = request.args.get("mode")
    crypx = request.args.get("crypx")

##### Service 2 (fiatgen) and Service 3 (Crypgen) Calls  ##### 

    fiatfull = requests.get('http://fiatgen:5001/randomfiat?region={0}'.format(region)) # Requests information from s2 using passed URL Variables for Region
    crypfull = requests.get('http://crypgen:5002/randomcryp?crypx={0}'.format(crypx)) # Requests information from s3 using passed URL Variables for Crypto List
    fiatfull = fiatfull.text # Extracts text information from fiatgen s2
    crypfull = crypfull.text # Extracts text information from crypgen s3

    fiatlist = fiatfull.split(":") # Splits text information at Colons for Fiat info returned 
    fiatabv = fiatlist[0]          # Fiat Abbreviation

    cryplist = crypfull.split(":") # Splits text information at Colons for Crypto info returned
    crypabv = cryplist[0]          # Crypto Abbreviation

    
    if mode == '0' or mode == '1':      # If mode chosen is Cryp2Fiat
        val_from = crypabv              # External API Variable for From Symbol (fsym) is Cryp
        val_to = fiatabv                # External API Variable for To Symbol (tsym) is Fiat
        abvpair = crypfull + fiatfull   # String to return to Service 1 -> e.g. BTC:Bitcoin:GBP:Great Britian Pound:
    else:                               # If mode chosen is Fiat2Cryp
        val_from = fiatabv              # External API Variable for From Symbol (fsym) is Fiat
        val_to = crypabv                # External API Variable for To Symbol (tsym) is Cryp
        abvpair = fiatfull + crypfull   # String to return to Service 1 -> e.g. GBP:Great Britian Pound:BTC:Bitcoin:


##### External API Call (CryptoCompare) #####

## URL Creation Using Chosen Variables for Symbol From and Symbol To:

    baseurl = "https://min-api.cryptocompare.com/data/price?"
    endurl = "fsym="+val_from+"&tsyms="+val_to
    apikey = "&api_key="
    url = baseurl+endurl+apikey+secretkey


    currency = requests.get(url)
    currency = currency.text

## Extracting Price Information From Dictionary Returned e.g {"GBP":5534.91}

    currency = ast.literal_eval(currency)
    dictlist =[]
    for key, value in currency.items():
        dictlist.append(value)
    value = dictlist[0]  # Extracts Price Only

    ### Creates String to Return back to Service 1 ###

    fullpair = abvpair + str(value)  ### Generates String in Format -> Fiat ABV : Full Name of Fiat e.g. GBP:Great Britian Pound

    return fullpair