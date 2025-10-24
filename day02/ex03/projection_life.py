from load_csv import load
import matplotlib.pyplot as plt
import numpy as np


def display_graph(path_ipp: str, path_ley, year: str):
    """take 2 file_path.csv: str, and a year: str
    displays the projection of life expectancy
    in relation to the gross national product of
    the year 1900 for each country."""
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
