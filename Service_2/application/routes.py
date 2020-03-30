from application import app
import random
import csv

@app.route('/randomfiat', methods=['GET'])
def fiat():

    list = []

    with open('fiatfull.csv', 'r') as csv_file:
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


