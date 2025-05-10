import pandas as pd

def load_prices_from_csv(filepath):
    df = pd.read_csv(filepath, index_col=0, parse_dates=True)
    return df.dropna()