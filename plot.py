import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("istherecorrelation.csv", sep=";", dtype=str)

year = df.iloc[:, 0]
student_count = df.iloc[:, 1]
beer_consumed = df.iloc[:, 2]

plt.plot(year, student_count, label='Student Count x1000', color='blue')
plt.plot(year, beer_consumed, label='Beer Consumed x1000 hL', color='orange')
plt.savefig('plot.png', dpi=300)
plt.xlabel('Year')
plt.ylabel('Value (x1000)')
plt.legend()
plt.show()