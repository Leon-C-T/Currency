from application import app
from flask import render_template, request
import random
import csv

@app.route('/randomcryp', methods=['GET'])
def crypto():

    crypx = request.args.get("crypx")
    crypx = int(crypx)

    list = []

    if crypx == 1:         ## Top 10 Coins
        with open('crypfiles/crypten.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                x = line
                list.append(x)

    elif crypx == 2:       ## Popular 30 Coins
        with open('crypfiles/cryppop30.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                x = line
                list.append(x)

    elif crypx == 3:       ## Top 50 Coins 
        with open('crypfiles/cryp50.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                x = line
                list.append(x)

    elif crypx == 4:       ## Top 100 Coins
        with open('crypfiles/cryphund.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                x = line
                list.append(x)      

    num = len(list)
    crypchosen = list[random.randrange(num)]

    crypstring =""
    for i in crypchosen:
        crypstring = crypstring + i + ":"            


    return crypstring