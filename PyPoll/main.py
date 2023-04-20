import os
import csv

path = "Resources/election_data.csv"
election = open(path)

my_Report = open('analysis/Report.txt', 'w')

csv_file = csv.reader(election)

#total number votes cast
cast = 0
cast2 = 0
for line in csv_file:
    cast += 1
# print(cast-1)
cast2 = cast -1

#how many votes each candidate received
charles = 0
diana = 0
raymon = 0
charles2 = diana2 = raymon2 = 0

election = open(path)
csv_dict = csv.DictReader(election)

for line in csv_dict:
    if line['Candidate'] == 'Raymon Anthony Doane':
        raymon += 1
    elif line['Candidate'] == 'Diana DeGette':
        diana += 1
    elif line['Candidate'] == 'Charles Casper Stockham':
        charles += 1
# print(raymon)
# print(diana)
# print(charles)

charles2 = charles
diana2 = diana
raymon2 = raymon

#the percentage of votes each candidate won
charlesper = 0
dianaper = 0
raymonper = 0

charlesper = (charles/cast)*100
dianaper = (diana/cast)*100
raymonper = (raymon/cast)*100

# print(charlesper)
# print(dianaper)
# print(raymonper)

output=f'''
Election Results
-------------------------
Total Votes: {cast2}
-------------------------
Charles Casper Stockham: {charlesper:,.2f}% {charles2:,}
Diana DeGette: {dianaper:,.2f}% {diana2:,}
Raymon Anthony Doane: {raymonper:,.2f}% {raymon2:,}
-------------------------
Winner: Diana DeGette
-------------------------
'''

print(output)
my_Report.write(output)