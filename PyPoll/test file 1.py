import os
import csv
budget_csv = os.path.join('..',"Resources", "budget_data.csv")
with open(budget_csv, 'r') as budget_csv:
	csv_reader = csv.reader(budget_csv,delimiter=",")
	next(csv_reader)
#Variable
months = 0
total_profit = 0
average_change = 0
greatest_increase = ["Mon-dd", 0]
greatest_decrease = ["Mond-dd", 0]
old_row = 0
new_row = 0
change = 0

