import os
import csv
output = os.path.join("","output","new.csv")
budget_csv = os.path.join("","Resources","budget_data.csv")

with open (budget_csv,'r') as budget_csv:
    csv_reader = csv.reader(budget_csv,delimiter=",")
    csv_header = next(csv_reader)
    print(f"Header:{csv_header}")

    #variable
    months = 0
    total_months=0
    total_profit = []
    average_change = 0
    greatest_increase = ("mon-dd",0)
    greatest_decrease = ("mon-dd",0)
    prior_profit = 0
    difference =[]
    date=[]
    
    # total months included
    for row in csv_reader:
        months +=1
        total_months += int(row[1])
 
        #net total amount of profitloss
        date.append(row[0])
        profit = int(row[1]) 
        total_profit.append(profit)
        
        #chang in profitloss over period
        proloss=0 
        if prior_profit != 0: 
            proloss = profit - prior_profit
            difference.append(proloss)
        print(total_months)
        print(total_profit)
        print(difference)