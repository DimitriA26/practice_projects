import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("sales.csv")




plt.plot(df["day"],df["income"], color = "green")
plt.grid(True)
plt.title("Sales per day for the month of January.")
plt.xticks(np.arange(0,31,2))
plt.yticks(np.arange(0,100000,5000))
plt.xlim(0,31)
plt.ylim(0,100000)
plt.plot(df["day"],df["income"], color = "green")

plt.show()


