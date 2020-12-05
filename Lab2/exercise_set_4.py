#
# NumPy exercises
#
import pandas as pd
import matplotlib.pyplot as plt



# The JSON module is used to convert the python dictionary into a JSON string that can be written into a file

def es_1():
    data = pd.read_csv("../resources/sales_data.csv")
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


def es_2():
    df = pd.read_csv("../resources/sales_data.csv")
    profit_list = df["total_profit"].values
    months = df["month_number"].values
    plt.figure()
    plt.plot(months, profit_list, label="profit data of the last year", color='r',
             marker='o', markerfacecolor='k', linestyle='--', linewidth=3)
    plt.xlabel("month number")
    plt.ylabel("Profit in dollar")
    plt.legend(loc="lower right")
    plt.title("Company Sales data of last year")
    plt.xticks(months)
    plt.yticks([100e3, 200e3, 300e3, 400e3, 500e3])
    plt.show()


def es_3():
    df = pd.read_csv("../resources/sales_data.csv")
    facecream = df["facecream"].values
    facewash = df["facewash"].values
    toothpaste = df["toothpaste"].values
    bathingsoap = df["bathingsoap"].values
    shampoo = df["shampoo"].values
    moisturizer = df["moisturizer"].values
    months = df["month_number"].values
    plt.figure()
    plt.plot(months, facecream, label="Face Cream Sales Data", marker='o', linewidth=3)
    plt.plot(months, facewash, label="Face Wash Sales Data", marker='o', linewidth=3)
    plt.plot(months, toothpaste, label="Toothpaste Sales Data", marker='o', linewidth=3)
    plt.plot(months, bathingsoap, label="Bathing Soap Sales Data", marker='o', linewidth=3)
    plt.plot(months, shampoo, label="Shampoo Sales Data", marker='o', linewidth=3)
    plt.plot(months, moisturizer, label="Moisturizer Sales Data", marker='o', linewidth=3)
    plt.xlabel("month number")
    plt.ylabel("Sales units in number")
    plt.legend(loc="upper left")
    plt.xticks(months)
    plt.show()


def es_4():
    # Read toothpaste sales data of each month and show it using a scatter plot
    df = pd.read_csv("../resources/sales_data.csv")
    toothpaste = df["toothpaste"].values
    months = df["month_number"].values
    plt.scatter(months, toothpaste, label="Toothpaste Sales Data")
    plt.xlabel("month number")
    plt.ylabel("Toothpaste sales data")
    plt.xticks(months)
    plt.grid(True, linewidth=0.5, linestyle='--')
    plt.show()


def es_5():
    df = pd.read_csv("../resources/sales_data.csv")
    months = df["month_number"].values
    bathingsoap = df["bathingsoap"].values
    plt.bar(months, bathingsoap, label="Bathing Soap Sales Data")
    plt.xlabel("months")
    plt.ylabel("Sales units")
    plt.xticks(months)
    plt.grid(True, linewidth=0.5, linestyle='--')
    plt.show()


def es_6():
    df = pd.read_csv("..resources/sales_data.csv")
    profit_list=df['total_profit'].values
    plt.figure()
    profit_range = [150e3, 175e3, 200e3, 225e3, 250e3, 300e3, 350e3]
    plt.hist(profit_list, profit_range, label='Profit data')
    plt.xlabel('profit range [$]')
    plt.ylabel('Actual Profit [$]')
    plt.legend(loc='upper left')
    plt.xticks(profit_range)
    plt.title('Profit data')
    plt.show()

def es_7():
    df = pd.read_csv("..resources/sales_data.csv")
    months = df['month_number'].values
    bathing_soap = df['bathingsoap'].values
    face_wash_sales_data = df['facewash'].values
    f, axs = plt.subplots(2, 1, sharex=True)
    axs[0].plot(months, bathing_soap, label='Bathing soap sales data',
                color ='k', marker ='o', linewidth = 3)
    axs[0].set_title('Sales data of a bathing soap')
    axs[0].grid(True, linewidth=0.5, linestyle='--')
    axs[0].legend()
    axs[1].plot(months, face_wash_sales_data, label='Face wash sales data',
                color ='r', marker ='o', linewidth = 3)
    axs[1].set_title('Sales data of a face wash')
    axs[1].grid(True, linewidth=0.5, linestyle='--')
    axs[1].legend()
    plt.xticks(months)
    plt.xlabel('Month number')
    plt.ylabel('Sales units in number')
    plt.show()



    if __name__ == "__main__":
    print("\n------- Exercise set 3, NumPy --------")
    print("\n Exercise 1")
    es_1()
    print("\n Exercise 2")
    es_2()
    print("\n Exercise 3")
    es_3()
    print("\n Exercise 4")
    es_4()
    print("\n Exercise 5")
    es_5()
    print("\n Exercise 6")
    es_6()
    print("\n Exercise 7")
    es_7()