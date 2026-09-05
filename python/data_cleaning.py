import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
INPUT = BASE / "data" / "SuperMarket Analysis.csv"
OUTPUT = BASE / "data" / "cleaned_supermarket_sales.csv"

df = pd.read_csv(INPUT)

print("Shape:", df.shape)
print("\nData types:\n", df.dtypes)
print("\nMissing values:\n", df.isna().sum())
print("\nDuplicate rows:", df.duplicated().sum())

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["Time_dt"] = pd.to_datetime(df["Time"], format="%I:%M:%S %p", errors="coerce")
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Month Name"] = df["Date"].dt.month_name()
df["Day"] = df["Date"].dt.day
df["Day of Week"] = df["Date"].dt.day_name()
df["Hour"] = df["Time_dt"].dt.hour

# Remove exact duplicate records and invalid date/time rows if present.
df = df.drop_duplicates()
df = df.dropna(subset=["Date", "Time_dt"])

df = df.drop(columns=["Time_dt"])
df.to_csv(OUTPUT, index=False)

print("\nCleaned shape:", df.shape)
print("Saved:", OUTPUT)
