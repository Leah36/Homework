import os
import csv

files_to_load = os.path.join("budget_data.csv")

total_months = 0
total_PL = 0

with open(files_to_load) as budget_data:
    csvreader = csv.reader(budget_data)

    header = next(csvreader)
    print(header)

    first_row = next(csvreader)
    print(first_row)

    total_months = total_months + 1
    total_PL = total_PL + int(first_row[1])
    prev_value = int(first_row[1])

    for row in csvreader:
        total_months = total_months + 1
        total_PL + total_PL + int(row[1])

    print(total_months)
    print(total_PL)
    print(prev_value)


