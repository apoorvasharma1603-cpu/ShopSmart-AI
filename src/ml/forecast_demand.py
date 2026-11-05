from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error
from statsmodels.tsa.holtwinters import ExponentialSmoothing

from src.ml.forecast_data import split_orders

CHART_DIR = Path(__file__).resolve().parent.parent.parent / "docs" / "forecast"
CHART_DIR.mkdir(parents=True, exist_ok=True)

TEST_DAYS = 14

train, test = split_orders(test_days=TEST_DAYS)
print(f"Training: {train.index[0].date()} to {train.index[-1].date()} ({len(train)} days)")
print(f"Test:     {test.index[0].date()} to {test.index[-1].date()} ({len(test)} days)")
print()


def errors(actual, forecast):
    """Return the two error measures: MAE and RMSE (lower is better)."""
    mae = mean_absolute_error(actual, forecast)
    rmse = mean_squared_error(actual, forecast) ** 0.5
    return mae, rmse


# ---------- Forecast 1: a simple baseline ("same as the same day last week") ----------
last_week = train.iloc[-7:].to_numpy()
baseline = pd.Series(np.tile(last_week, 2), index=test.index)[:TEST_DAYS]

# ---------- Forecast 2: Holt-Winters WITHOUT the weekly pattern ----------
no_season = ExponentialSmoothing(train, trend="add", seasonal=None).fit()
no_season_forecast = no_season.forecast(TEST_DAYS)

# ---------- Forecast 3: Holt-Winters WITH the weekly pattern ----------
model = ExponentialSmoothing(train, trend="add", seasonal="add", seasonal_periods=7).fit()
forecast = model.forecast(TEST_DAYS)

# ---------- Compare them ----------
results = pd.DataFrame(
    {
        "baseline (same day last week)": errors(test, baseline),
        "Holt-Winters, no weekly pattern": errors(test, no_season_forecast),
        "Holt-Winters, with weekly pattern": errors(test, forecast),
    },
    index=["MAE", "RMSE"],
).T.round(2)

print(f"Forecasting the next {TEST_DAYS} days and comparing with what really happened:")
print()
print(results)
print()
print(f"The Holt-Winters forecast is off by about {results.loc['Holt-Winters, with weekly pattern', 'MAE']:.1f} orders a day on average.")
print()

print("Day-by-day, with weekly pattern:")
table = pd.DataFrame({"actual": test, "forecast": forecast.round(1)})
table["error"] = (table["actual"] - table["forecast"]).round(1)
print(table.to_string())
print()

# ---------- Chart: the forecast against reality ----------
#plt.figure(figsize=(10, 4))
#history = train.iloc[-42:]
#plt.plot(history.index, history, label="Training data (last 6 weeks)", color="steelblue")
#plt.plot(test.index, test, label="What really happened", color="black", marker="o")
#plt.plot(test.index, forecast, label="Holt-Winters forecast", color="red", linestyle="--", marker="o")
#plt.plot(test.index, baseline, label="Baseline (same day last week)", color="grey", linestyle=":")
#plt.title("Forecasting the Next 28 Days of Orders")
#plt.xlabel("Date")
#plt.ylabel("Orders")
#plt.legend(loc="upper center", bbox_to_anchor=(0.5, -0.2), ncol=2)  # legend below the chart
#plt.tight_layout()
#plt.savefig(CHART_DIR / "2_forecast_vs_actual.png")
#plt.close()
#print(f"Saved chart to {CHART_DIR}")
