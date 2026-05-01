import csv

with open('color_srgb.csv', 'r') as csvfile:
    reader=csv.reader(csvfile, delimiter=',')
    for row in reader:
        print(type(row))
        print(row)