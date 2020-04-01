from application import app
from flask import render_template, request
import random
import csv

@app.route('/randomfiat', methods=['GET'])
def fiat():


    region = request.args.get("region")
    region = int(region)


    if region == 1:             ## No Region Selected (Random)
        list = []

        with open('fiatfull.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            
            for line in csv_reader:
                x = line
                list.append(x)

    elif region == 2:       ## European Region 
        list = [['GBP', 'Great Britian Pound'], ['EUR', 'Euros'], ['CHF', 'Switzerland Franc'], ['RUB', 'Russian Ruble'], ['DKK', 'Danish krone'], ['SEK', 'Swedish krona']]
    elif region == 3:       ## Oceania Region 
        list = [['AUD', 'Australia Dollar'], ['NZD', 'New Zealand dollars']]
    elif region == 4:       ## North American Region
        list = [['USD', 'USA Dollar'], ['CAD', 'Canadian Dollar'], ['MXN' ,'Mexican Pesos']]
    elif region == 5:       ## South American Region
        list = [['ARS', 'Argentine pesos'], ['BRL', 'Brazilian real']]
    elif region == 6:       ## West and South Asian Region
        list = [['INR', 'Indian Rupee'],  ['AED', 'UAE Dirhams'], ['IRR', 'Iranian rials'], ['OMR', 'Omani Rials'], ['QAR', 'Qatari riyals'], ['SAR', 'Saudi riyal'], ['TRY', 'Turkish Lira']]
    elif region == 7:       ## North and East Asian Region
        list = [['CNY', 'China Yuan'], ['JPY', 'Japan Yen'], ['KRW' ,'South Korean Won'], ['SGD', 'Singapore dollars']]
    elif region == 8:       ## African Region
        list = [['ZAR', 'Rand'], ['EGP', 'Egyptian pounds'], ['NGN', 'Nigerian Naira']]


    num = len(list)
    fiatchosen = list[random.randrange(num)]

    fiatstring =""
    for i in fiatchosen:
        fiatstring = fiatstring + i + ":"

    print(fiatstring)
    
    return fiatstring

    




