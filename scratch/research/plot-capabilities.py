"""Rebuild the capability-index slide from the dated Epoch AI CSV snapshot."""

import csv
import os
from datetime import datetime
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/fac-vibing-matplotlib")
import matplotlib

matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "links/epoch-2026-09-20/eci_scores.csv"
OUT = ROOT / "slides/images/epoch-eci-2026-09-20.png"
with DATA.open() as f:
    rows = [r for r in csv.DictReader(f) if r["date"] >= "2023-01-01"]

fig, ax = plt.subplots(figsize=(12, 4.8), layout="constrained")
fig.set_facecolor("#fffdf8")
ax.set_facecolor("#fffdf8")
ax.scatter(
    [datetime.fromisoformat(r["date"]) for r in rows],
    [float(r["eci"]) for r in rows],
    color="#9da9a4", alpha=0.55, s=18, linewidths=0,
)
labels = {
    "GPT-4 (Mar 2023)": (12, 12, "GPT-4"),
    "GPT-4o (May 2024)": (-5, -25, "GPT-4o"),
    "o1": (-28, 12, "o1"),
    "GPT-5": (-10, -26, "GPT-5"),
    "GPT-6 Astra": (-120, 13, "GPT-6 Astra"),
    "Claude Fable 5.1": (-135, -26, "Claude Fable 5.1"),
}
for row in rows:
    if row["Model"] not in labels:
        continue
    x, y = datetime.fromisoformat(row["date"]), float(row["eci"])
    dx, dy, name = labels[row["Model"]]
    ax.scatter([x], [y], s=45, color="#276bca", zorder=3)
    ax.annotate(name, (x, y), xytext=(dx, dy), textcoords="offset points",
                fontsize=13, color="#17201f")
ax.set_xlim(datetime(2023, 1, 1), datetime(2026, 12, 1))
ax.set_ylim(top=max(float(r["eci"]) for r in rows) + 15)
ax.set_ylabel("Epoch Capabilities Index", fontsize=13)
ax.set_xlabel("Model release date", fontsize=12)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
ax.tick_params(labelsize=12)
ax.spines[["top", "right"]].set_visible(False)
ax.grid(axis="y", alpha=0.18)
ax.set_axisbelow(True)
fig.suptitle("Model capability scores since 2023", fontsize=17, x=0.06, ha="left")
fig.text(0.99, 0.01, "Source: Epoch AI · 20 Sep 2026 snapshot · CC BY 4.0",
         ha="right", fontsize=9, color="#5c6763")
fig.savefig(OUT, dpi=160, facecolor=fig.get_facecolor())
plt.close(fig)
print(OUT)
