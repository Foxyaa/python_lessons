import csv
from collections import Counter
lst = []
with open(r"C:\Users\79537\Downloads\Crimes.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if '2015' in row["Date"]:
            lst += [row['Primary Type']]
d=Counter(lst)
print(d)