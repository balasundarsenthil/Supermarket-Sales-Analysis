import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data" / "cleaned_supermarket_sales.csv"
OUT = BASE / "outputs" / "charts"
OUT.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA, parse_dates=["Date"])

print("Total Revenue:", round(df["Sales"].sum(), 2))
print("Total Gross Income:", round(df["gross income"].sum(), 2))
print("Transactions:", df["Invoice ID"].nunique())
print("Quantity Sold:", int(df["Quantity"].sum()))
print("Average Transaction Value:", round(df["Sales"].mean(), 2))

analyses = {
    "sales_by_product_line": df.groupby("Product line")["Sales"].sum().sort_values(ascending=False),
    "profit_by_product_line": df.groupby("Product line")["gross income"].sum().sort_values(ascending=False),
    "sales_by_branch": df.groupby("Branch")["Sales"].sum().sort_values(ascending=False),
    "sales_by_gender": df.groupby("Gender")["Sales"].sum().sort_values(ascending=False),
    "sales_by_customer_type": df.groupby("Customer type")["Sales"].sum().sort_values(ascending=False),
    "sales_by_payment": df.groupby("Payment")["Sales"].sum().sort_values(ascending=False),
}

for name, series in analyses.items():
    ax = series.plot(kind="bar", title=name.replace("_", " ").title())
    plt.tight_layout()
    plt.savefig(OUT / f"{name}.png", dpi=160)
    plt.close()

monthly = df.groupby(df["Date"].dt.to_period("M"))["Sales"].sum()
monthly.plot(marker="o", title="Monthly Sales Trend")
plt.tight_layout()
plt.savefig(OUT / "monthly_sales_trend.png", dpi=160)
plt.close()

print("\nAnalysis complete.")
