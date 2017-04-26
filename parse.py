import csv
with open('C:\RPSR13Q4.txt', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='$', quotechar='|')
    for row in spamreader:
      print ', '.join(row)
