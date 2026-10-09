import pandas as pd
import matplotlib.pyplot as plt

# decimal="," assumes European-style numbers; add thousands="." if values like "1.234" appear
df = pd.read_csv("istherecorrelation.csv", sep=";", decimal=",")
year, students, beer = (df.iloc[:, i] for i in range(3))

c1, c2 = "#1f77b4", "#e07b00"
fig, ax1 = plt.subplots(figsize=(9, 5))
ax2 = ax1.twinx()

l1, = ax1.plot(year, students, color=c1, marker="o", lw=2, label="Student count (×1000)")
l2, = ax2.plot(year, beer, color=c2, marker="s", lw=2, label="Beer consumed (×1000 hL)")

ax1.set_xlabel("Year")
ax1.set_ylabel("Student count (×1000)", color=c1)
ax2.set_ylabel("Beer consumed (×1000 hL)", color=c2)
ax1.tick_params(axis="y", colors=c1)
ax2.tick_params(axis="y", colors=c2)


# One combined legend instead of two overlapping ones
ax1.legend(handles=[l1, l2], loc="upper left",)

ax1.set_title(f"Students vs. beer consumption")

fig.tight_layout()
fig.savefig("plot.png", dpi=300)  
plt.show()