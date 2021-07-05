import math
import csv
with open('standarddaviation.csv',newline='') as f:
    reader = csv.reader(f)
    f_data = list(reader)

data = f_data[0]

def mean(data):
    n=len(data)
    total=0
    for x in data:
        total += int(x)
    mean = total/n
    return mean

squares = []
for number in data:
    a = int(number) - mean(data)
    a=a**2
    squares.append(a)
    sum=0
    for i in squares:
        sum = sum + 1

    result = sum/(len(data)-1)

    standarddaviation = math.sqrt(result)
    print(standarddaviation)