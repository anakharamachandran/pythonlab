import csv
with open('aru.txt') as inf:
 content = csv.DictReader(inf)

 print("playername")

 for row in content:
   print(row["PlayerName"])
    
