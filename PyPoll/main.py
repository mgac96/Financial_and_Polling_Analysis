import os
import csv

election_csv = os.path.join("Resources","Election_Data.csv")
total_votes = []
with open(election_csv,'r') as election_csv:
    csv_reader =csv.reader(election_csv,delimiter=",")
    next (csv_reader)
    row_count = 0
    for row in csv_reader:
            row_count += 1
    total_votes = row_count

    stockham = 0
    degette = 0
    doane = 0

    for row in csv_reader:
        if row[2] == "Charles Casper Stockham":
            stockham += 1
        elif row[2] == "Diana Degette":
            degette +=1
        elif row [2] =="Raymon Anthony Doane" :
            doane += 1

    stockham_percent = stockham / total_votes
    degette_percent = degette / total_votes
    doane_percent = doane / total_votes

    print("Election Results")