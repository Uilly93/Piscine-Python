import pandas as pd


def load(path: str) -> pd.DataFrame:
    """load file.csv from path: str parameter
    returns a pandas dataframe"""
    df = pd.read_csv(path)
    print(f"loading data set of dimension {df.shape}")
    return df
