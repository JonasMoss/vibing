# first try - means by group
import csv

rows = list(csv.DictReader(open("data.csv")))
for cond in ["monthly", "yearly"]:
    x = [float(r["wtp_nok"]) for r in rows if r["condition"] == cond]
    print(cond, sum(x) / len(x))
