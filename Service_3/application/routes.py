from application import app
from flask import render_template, request
import random
import csv

####################################### Start of App Route for Service 3 (crypgen) #######################################

@app.route('/randomcryp', methods=['GET'])
def crypto():

## Gets URL Variable for Crypto List from Service 4 (As selected by User in Service 1):
    crypx = request.args.get("crypx")
    crypx = int(crypx)

    list = []

### List Population:

    if crypx == 0 or crypx == 1:                                ## Top 10 Coins
        with open('crypfiles/crypten.csv', 'r') as csv_file:    ## Opens File in read mode
            csv_reader = csv.reader(csv_file)                   ## Read File 
            for line in csv_reader:                             ## Selects Line
                x = line
                list.append(x)                                  ## Populates list with all data in file (All Fiat currencies in File)

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

    num = len(list)                                         ## Returns length of list and assign to variable
    crypchosen = list[random.randrange(num)]                ## Randomly selects a fiat currency from the list

### Creates String to Return back to Service 4 ###

    crypstring =""
    for i in crypchosen:
        crypstring = crypstring + i + ":"                   ### Generates String in Format -> Cryp ABV : Full Name of crypto e.g. BTC:Bitcoin


    return crypstring