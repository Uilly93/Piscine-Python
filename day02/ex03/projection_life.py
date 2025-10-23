from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def display_graph(path_ipp: str, path_ley):
    ipp = load(path_ipp)
    ley = load(path_ley)
    ipp = ipp["1900"].to_numpy()
    ley = ley["1900"].to_numpy()
    print(ipp)
    print(ley)
