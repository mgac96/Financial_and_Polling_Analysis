# First we have to import OS Module to allow cross operating systems 
import os
import csv
budget_csv = os.path.join("Resources","budget_data.csv")
with open (budget_csv,'r') as budget_csv:
    csv_reader = csv.reader(budget_csv,delimiter=",")
    next(csv_reader)
    row_count = 0
    for row in csv_reader:
        row_count +=1
    print(f'Total:{row_count}')
#Identify variable
months = 0
total_profit = 0
average_change = 0 
greatest_increase = ["Mon-dd",0]
greatest_decrease = ["Mon-dd",0]
old_row = 0
new_row = 0
change = 0
for i,row in enumerate(csv_reader):
        if i == 1:
            for value in row:
                sum += int(value)
print(f'net total:{sum}')
value = row[1]
total = 0
for row in csv_reader:
        for value in row:
            total += float(value)
print({total})


   