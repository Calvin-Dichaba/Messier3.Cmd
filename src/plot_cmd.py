import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load dataset
df = pd.read_csv("../data/gagainstg-i.txt", sep="\t", header=None, names=["g", "g-i"])

# Scatter plot
plt.figure(figsize=(6, 8))
plt.scatter(df["g-i"], df["g"], s=2)

plt.xlabel("g - i")
plt.ylabel("g")
plt.title("Color-Magnitude Diagram – Messier 3")

# Reverse y-axis for CMD
plt.gca().invert_yaxis()

# x-axis range
plt.xlim(-0.8, 1.6)
plt.xticks(np.arange(-0.8, 1.7, 0.2))

plt.grid(True)
plt.tight_layout()
plt.show()
