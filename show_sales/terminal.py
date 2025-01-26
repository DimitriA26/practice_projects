import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys




df = pd.read_csv("sales.csv")


def show_data():
    plt.plot(df["day"],df["income"], color = "green")
    plt.grid(True)
    plt.title("Sales per day for the month of January.")
    plt.xticks(np.arange(0,31,2))
    plt.yticks(np.arange(0,100000,5000))
    plt.xlim(0,31)
    plt.ylim(0,100000)
    plt.plot(df["day"],df["income"], color = "green")

    plt.show()



def print_data():
    print(df)




print("Main menu.\n Please choose from list of options:\n1: Read data.\n2: Graph data.\n3. Quit")
while True:
    
    response = input("Option:")

    if response == "1":
        print_data()

    elif response == "2":
        show_data()

    elif response == "3":
        print("Closing Menu.")
        sys.exit()
        break

    else:
        print("Invalid option. Please try again.")
        continue
    n = input("Press any key to continue: ")
    print("Main menu.\n Please choose from list of options:\n1: Read data.\n2: Graph data.\n3. Quit")