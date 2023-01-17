import os
import csv
#variable 
total_profit = 0
greatest_increase = ("mon-dd",0)
greatest_decrease = ("mon-dd",0)
months = 0
old = 0
new = 0
change = 0
average_change = 0

output = os.path.join("", "output.csv")
budget_csv = os.path.join("","Resources","budget_data.csv")

with open (budget_csv,'r') as budget_csv:
    csv_reader = csv.reader(budget_csv,delimiter=",")
    csv_header = next(csv_reader)
    
    with open(output, 'w') as csvfile:
        csvwriter = csv.writer(csvfile,delimiter=",")
        csvwriter.writerow(csv_header)
#months in dataset
    for row in csv_reader:
        months += 1
#net profit
    total_profit = total_profit + int(row[1])
#change in profit loss
    if old == 0:
        csvwriter.writerow([row[0],row[1],0])
        old = int(row[1])
    else:
        new = int(row[1])
        change = new - old
        csvwriter.writerow([row[0],row[1],change])
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
    summaryfile = os.path.join("","Analysis","summary.txt")
    with open(summaryfile,w) as f:
        f.write("summary")
        f.write(f"\nTotal months: {months}")
        f.write(f"\nTotal profit : {total_profit}")
        f.write(f"\nGreatestIncrease : {greatest_increase}")
        f.write(f"\nGreatestDecrease : {greatest_decrease}")
        f.write(f"\n Average change : {average_change}")
    with open(summaryfile,'r') as text:
        lines = text.read()
        print(lines)
    

