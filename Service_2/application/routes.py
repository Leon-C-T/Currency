from application import app
from flask import render_template, request
import random
import csv

@app.route('/randomfiat', methods=['GET'])
def fiat():


    region = request.args.get("region")
    region = int(region)

    list = []

    if region == 0 or region == 1:         ## No Region Selected (Random)
        with open('fiatfiles/fiatfull.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                x = line
                list.append(x)

    elif region == 2:       ## European Region 
        with open('fiatfiles/fiateur.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                x = line
                list.append(x)

    elif region == 3:       ## Oceania Region 
        with open('fiatfiles/fiatoceania.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                x = line
                list.append(x)

    elif region == 4:       ## North American Region
        with open('fiatfiles/fiatna.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                x = line
                list.append(x)

    elif region == 5:       ## South American Region
        with open('fiatfiles/fiatsa.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                x = line
                list.append(x)

    elif region == 6:       ## West and South Asian Region
        with open('fiatfiles/fiatasiaws.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                x = line
                list.append(x)

    elif region == 7:       ## North and East Asian Region
        with open('fiatfiles/fiatasiane.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                x = line
                list.append(x)

    elif region == 8:       ## African Region
        with open('fiatfiles/fiatafrica.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                x = line
                list.append(x)

    

    num = len(list)
    fiatchosen = list[random.randrange(num)]

    fiatstring =""
    for i in fiatchosen:
        fiatstring = fiatstring + i + ":"

    print(fiatstring)
    
    return fiatstring

    




