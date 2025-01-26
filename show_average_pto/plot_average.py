import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("pto.csv")




def plot_average():

    avg_pto = df.groupby("age")["pto_used"].mean()
    print(avg_pto)

    plt.plot(avg_pto.index, avg_pto.values, color = "blue", marker = "o")
    plt.grid(True)
    plt.xticks(np.arange(20,40,2))
    plt.yticks(np.arange(0,31,2))
    plt.xlim(20,40)
    plt.ylim(0,31)
    plt.show()


plot_average()