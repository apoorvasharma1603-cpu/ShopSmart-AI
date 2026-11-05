from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # save charts as files instead of opening windows
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

from src.ml.forecast_data import load_orders

CHART_DIR = Path(__file__).resolve().parent.parent.parent / "docs" / "forecast"
CHART_DIR.mkdir(parents=True, exist_ok=True)

orders = load_orders()

# Pull the series apart into trend + weekly pattern + leftover noise
parts = seasonal_decompose(orders, model="additive", period=7)

figure = parts.plot()
figure.set_size_inches(9, 7)
plt.tight_layout()
plt.savefig(CHART_DIR / "1_decomposition.png")
plt.close()

trend = parts.trend.dropna()
print(f"Days in the data: {len(orders)}")
print(f"Trend near the start: {trend.iloc[0]:.1f} orders a day")
print(f"Trend near the end:   {trend.iloc[-1]:.1f} orders a day")
print()
print("Weekly pattern (how far each day of the 7-day cycle sits above or below the trend):")
weekly = parts.seasonal.iloc[:7]
for date, effect in weekly.items():
    print(f"  {date.day_name():<9} {effect:+.1f}")
print()
print(f"Typical size of the leftover noise: about {parts.resid.dropna().std():.1f} orders")
print(f"Saved chart to {CHART_DIR}")
