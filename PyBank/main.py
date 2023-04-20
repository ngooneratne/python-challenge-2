import os
import csv

path = "Resources/budget_data.csv"
my_report = open('analysis/Report.txt', 'w')

months = 0
total = 0
total_ch = 0
prev_rev = 0
inc = ['',0]
dec = ['',0]

budget = open(path)
csv_dict = csv.DictReader(budget)

for row in csv_dict:
    months += 1
    rev = int((row["Profit/Losses"]))
    total += rev

    change = rev - prev_rev
    if prev_rev == 0:
        change = 0
    
    total_ch += change
    prev_rev = rev

    if change > inc[1]:
        inc[0] = row['Date']
        inc[1] = change
    
    if change < dec[1]:
        dec[0] = row['Date']
        dec[1] = change

output = f'''
Financial Analysis
----------------------------
Total Months: {months}
Total: ${total:,}
Average Change: ${total_ch/(months-1):,.2f}
Greatest Increase in Profits: {inc[0]} (${inc[1]:,})
Greatest Decrease in Profits: {dec[0]} (${dec[1]:,})
'''

print(output)
my_report.write(output)