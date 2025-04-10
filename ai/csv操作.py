import csv
filename = 'ai/1.csv'
header_row=[]
with open(filename) as f:
    reader = csv.reader(f)
    for index,column_header in  enumerate(next(reader)):
        header_row.append(column_header)
    # header_row.append(next(reader)) 


print(header_row)