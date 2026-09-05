import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/SuperMarket Analysis.csv")

print("Dataset Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 Records:")
print(df.head())

print("\nTotal Sales:", df["Sales"].sum())
print("Average Sales:", df["Sales"].mean())

print("\nSales by Branch:")
print(df.groupby("Branch")["Sales"].sum().sort_values(ascending=False))

print("\nSales by Product Line:")
print(df.groupby("Product line")["Sales"].sum().sort_values(ascending=False))

print("\nSales by Payment:")
print(df.groupby("Payment")["Sales"].sum().sort_values(ascending=False))

print("\nSales by Gender:")
print(df.groupby("Gender")["Sales"].sum().sort_values(ascending=False))

print("\nSales by Customer Type:")
print(df.groupby("Customer type")["Sales"].sum().sort_values(ascending=False))

print("\nAverage Rating:", df["Rating"].mean())

# Branch chart
df.groupby("Branch")["Sales"].sum().plot(
    kind="bar",
    title="Sales by Branch"
)
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# Product line chart
df.groupby("Product line")["Sales"].sum().sort_values().plot(
    kind="barh",
    title="Sales by Product Line"
)
plt.xlabel("Sales")
plt.tight_layout()
plt.show()