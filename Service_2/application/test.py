import random
import csv
list = []
with open('fiatcur.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    for line in csv_reader:
        x = line
        list.append(x)
        
    num = len(list)
    y = list[random.randrange(num-1)]
    
    print(list)
    print(y)


