import numpy as np
np.set_printoptions(suppress=True)
print(np.arange(-1, 1, 0.1))


import matplotlib.pyplot as plt
import numpy as np
np.set_printoptions(suppress=True)
import pandas as pd

df = pd.read_csv("data.csv")
print(df)

salaries = df["salary"]
print(salaries)

df["tax"] = df["salary"] * 0.23
print(df)
x = []
for i in (np.arange(-10, 10.1, 0.1)):
    x.append(i)
y = []
for i in x:
    y.append(i*i*i-(2*i*i)+ (2*i)+1)

#for i in range(len(y)):
    #print([x[i], y[i]])
plt.plot(x, y, color='red', marker='.')
plt.grid(True)

plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Exponential growth plot")
plt.xticks(range(-1000,1000))
plt.yticks(range(-1000,1000))
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.legend()
#plt.show()
