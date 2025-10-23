import pandas as pd


def load(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    print(f"loading data set of dimension {df.shape}")
    return df
