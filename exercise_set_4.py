#
# NumPy exercises
#
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json


# The JSON module is used to convert the python dictionary into a JSON string that can be written into a file

def es_1():
    data = pd.read_csv("resources/sales_data.csv")
    profit_list = data["total_profit"].values
    months = data["month_number"].values
    plt.figure()
    plt.plot(months, profit_list, label="Profit data of last year")
    plt.xlabel("month")
    plt.ylabel("Profit")
    plt.xticks(months)
    plt.title("Company profit per month")
    plt.yticks([100e3, 200e3, 300e3, 400e3, 500e3])
    plt.show()


if __name__ == "__main__":
    print("\n------- Exercise set 3, NumPy --------")
    print("\n Exercise 1")
    es_1()
