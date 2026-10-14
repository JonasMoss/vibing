# analysis v2 - this is the one for table 1
import csv
import random
import statistics

rows = list(csv.DictReader(open("data_clean_FINAL.csv", encoding="utf-8"), delimiter=";"))

groups = {}
for r in rows:
    groups.setdefault(r["condition"], []).append(float(r["wtp_nok"]))
monthly, yearly = groups["monthly"], groups["yearly"]

diff = statistics.mean(monthly) - statistics.mean(yearly)

# permutation test, two-sided
random.seed(1)
pooled = monthly + yearly
hits = 0
draws = 10000
for _ in range(draws):
    random.shuffle(pooled)
    d = statistics.mean(pooled[:len(monthly)]) - statistics.mean(pooled[len(monthly):])
    if abs(d) >= abs(diff):
        hits += 1
p = hits / draws

lines = [
    "Table 1. Willingness to pay (NOK) by price framing",
    "",
    "condition     n     mean      sd",
]
for name, x in [("monthly", monthly), ("yearly", yearly)]:
    lines.append(f"{name:<10} {len(x):>4} {statistics.mean(x):>8.1f} {statistics.stdev(x):>7.1f}")
lines += [
    "",
    f"N = {len(rows)}",
    f"difference (monthly - yearly): {diff:.1f} NOK",
    f"permutation p-value ({draws:,} draws): {p:.3f}",
]
open("table1.txt", "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("\n".join(lines))
