from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def convert_value(array: np.ndarray):
    mult = {"k": 1000,
            "M": 1,
            "B": 1000}
    for i, v in enumerate(array):
        string = str(v)
        if string[-1] in ['k', 'M', 'B']:
            if string[-1] == 'k':
                array[i] = float(string[:-1]) / mult[string[-1]]
            else:
                array[i] = float(string[:-1]) * mult[string[-1]]
        else:
            array[i] = float(string)


def display_graph(path: str, country1: str, country2: str):
    """take the str: path of a data.csv and two str: countries
    displays the graphic of Population Projection from
    1800 to 2050"""
    df = load(path)
    ctr1 = df[df["country"].str.lower() == country1.lower()]
    ctr2 = df[df["country"].str.lower() == country2.lower()]
    year = df.columns[1:].astype(int)
    year = [v for v in year if v <= 2050]
    ctr1: np.ndarray = ctr1.iloc[0, 1:year.__len__() + 1].values
    ctr2: np.ndarray = ctr2.iloc[0, 1:year.__len__(
    ) + 1].values
    convert_value(ctr1)
    convert_value(ctr2)
    max_value = int(max(ctr1.max(), ctr2.max()) + 10)
    ticks = range(0, max_value, 20)
    label = [str(v) + 'M' for v in ticks]
    plt.plot(year, ctr1, "-b", label=country1.title())
    plt.plot(year, ctr2, "-g", label=country2.title())
    plt.legend(loc="lower right")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.xticks(range(1800, 2050, 40))
    plt.yticks(ticks, label)
    plt.title("Population Projections")
    plt.show()
