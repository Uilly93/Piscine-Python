from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def display_graph(path: str):
    df = load(path)
    fr = df[df["country"] == 'France']
    year = df.columns[1:].astype(int)
    mean = fr.iloc[0, 1:].values
    plt.plot(year, mean)
    plt.xlabel("Year")
    plt.ylabel("Value")
    plt.xticks(range(1800, 2100, 40))
    plt.show()
