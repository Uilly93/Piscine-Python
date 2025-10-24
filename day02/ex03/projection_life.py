from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def display_graph(path_ipp: str, path_ley, year: str):
    ipp = load(path_ipp)
    ley = load(path_ley)
    ipp = ipp[year].to_numpy()
    ley = ley[year].to_numpy()
    for age, amount in zip(ley, ipp):
        if not np.isnan(age):
            plt.plot(amount, age, 'o', color='C0')
    plt.xscale('log')
    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.title(year)
    plt.show()
