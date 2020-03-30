from application import app
import random
import csv

@app.route('/randomcryp', methods=['GET'])
def crypto():

    list = []

    with open('crypcur.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        for line in csv_reader:
            x = line
            list.append(x)

        print(list)    
        num = len(list)
        crypchosen = list[random.randrange(num)]

        crypstring =""
        for i in crypchosen:
            crypstring = crypstring + i + ":"

        print(crypstring)
        

    return crypstring