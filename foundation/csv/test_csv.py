# -*- coding: utf-8 -*-
import csv

with open('data.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'address', 'age'])
    data = [
        ('xiaoming ', 'china', '10'),
        ('Lily', 'USA', '12')]
    writer.writerows(data)

with open('data.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
