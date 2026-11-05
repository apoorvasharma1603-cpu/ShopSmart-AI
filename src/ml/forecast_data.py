from pathlib import Path

import pandas as pd

DATA_PATH = Path(__file__).resolve().parent.parent.parent / "data" / "orders.csv"


def load_orders():
    """Load the daily orders as a series with one value per day, in date order."""
    orders = pd.read_csv(DATA_PATH, parse_dates=["date"], index_col="date")
    return orders["orders"].asfreq("D")


def split_orders(test_days=14):
    """Split by time: everything except the last test_days is for training, the last test_days is the test."""
    orders = load_orders()
    train = orders.iloc[:-test_days]
    test = orders.iloc[-test_days:]
    return train, test
