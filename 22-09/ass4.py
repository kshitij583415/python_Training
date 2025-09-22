import csv

with open("f.csv", "r") as f:
    data = csv.reader(f)
    for i in data:
        print(i)
