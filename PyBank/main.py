import os
import csv
#variable 
total_profit = 0
greatest_increase = ["",0]
greatest_decrease = ["",999999999]
months = 0
old = 0
new = 0
change = 0
average_change = 0

output = os.path.join("","Analysis","output.txt")
budget_csv = os.path.join("","Resources","budget_data.csv")

with open (budget_csv) as budget_data:
    reader = csv.reader(budget_data,delimiter=",")
    header = next(reader)
    for row in reader:
    #months in dataset
            months += 1
    #net profit
            total_profit = total_profit + int(row[1])

        #change in profit loss
            if old == 0:
               old = int(row[1])
            else:
                new = int(row[1])
                change = new - old
                average_change += change
                old = new
                new = 0
    # greatest change in proft
            if change < greatest_decrease[1]:
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = change
            if change > greatest_increase[1]:
                greatest_increase[0] = row [0]
                greatest_increase[1] = change

    #average change
    average_change = round((average_change / (months -1)),2)
    #txt file
       
    
    with open(output,"w")as textfile:       
        summaryfile=(
            f"Total months: {months}\n"
            f"Total profit : {total_profit}\n"
            f"GreatestIncrease : {greatest_increase}\n"
            f"GreatestDecrease : {greatest_decrease}\n"
            f"Average change : {average_change}")
   
        print(summaryfile,end="")
        textfile.write(summaryfile)
   
        

