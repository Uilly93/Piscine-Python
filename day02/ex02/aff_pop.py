from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def display_graph(path: str):
    df = load(path)
    fr = df[df["country"] == 'France']
    year = df.columns[1:].astype(int)
    # year = [v in v ]
    frval = fr.iloc[0, 1:].values
    print(frval)
    plt.plot(year, frval)
    plt.xlabel("Year")
    plt.ylabel("Value")
    plt.xticks(range(1800, 2050, 40))
    # plt.yticks(range(2000000, 6000000, 2000000))
    plt.show()
