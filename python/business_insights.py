import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data" / "cleaned_supermarket_sales.csv"
REPORT = BASE / "outputs" / "reports" / "business_insights.md"

df = pd.read_csv(DATA, parse_dates=["Date"])

total_sales = df["Sales"].sum()
total_profit = df["gross income"].sum()
transactions = df["Invoice ID"].nunique()
avg_transaction = df["Sales"].mean()

branch = df.groupby("Branch").agg(Sales=("Sales","sum"), Profit=("gross income","sum"), Transactions=("Invoice ID","nunique")).sort_values("Sales", ascending=False)
product = df.groupby("Product line").agg(Sales=("Sales","sum"), Profit=("gross income","sum"), Quantity=("Quantity","sum")).sort_values("Sales", ascending=False)
customer = df.groupby("Customer type")["Sales"].sum().sort_values(ascending=False)
gender = df.groupby("Gender")["Sales"].sum().sort_values(ascending=False)
payment = df.groupby("Payment")["Sales"].sum().sort_values(ascending=False)
month = df.groupby(df["Date"].dt.to_period("M"))["Sales"].sum().sort_values(ascending=False)

lines = [
    "# Supermarket Sales — Business Insights",
    "",
    f"- Total revenue: **{total_sales:,.2f}**",
    f"- Total gross income: **{total_profit:,.2f}**",
    f"- Total transactions: **{transactions:,}**",
    f"- Average transaction value: **{avg_transaction:,.2f}**",
    "",
    f"1. **Top branch:** {branch.index[0]} with sales of {branch.iloc[0]['Sales']:,.2f}.",
    f"2. **Top product line by sales:** {product.index[0]} with {product.iloc[0]['Sales']:,.2f}.",
    f"3. **Top product line by gross income:** {product['Profit'].idxmax()} with {product['Profit'].max():,.2f}.",
    f"4. **Highest quantity product line:** {product['Quantity'].idxmax()} with {product['Quantity'].max():,} units.",
    f"5. **Largest customer segment:** {customer.index[0]} with sales of {customer.iloc[0]:,.2f}.",
    f"6. **Highest-sales gender segment:** {gender.index[0]} with sales of {gender.iloc[0]:,.2f}.",
    f"7. **Most-used payment method by transactions:** {df['Payment'].value_counts().idxmax()}.",
    f"8. **Highest-sales payment method:** {payment.index[0]} with {payment.iloc[0]:,.2f}.",
    f"9. **Strongest month:** {month.index[0]} with sales of {month.iloc[0]:,.2f}.",
    f"10. **Peak sales hour:** {df.groupby(df['Hour'])['Sales'].sum().idxmax()}:00 with sales of {df.groupby(df['Hour'])['Sales'].sum().max():,.2f}.",
    "",
    "## Recommendations",
    "",
    "- Protect inventory availability for the highest-performing product lines.",
    "- Use member-focused loyalty campaigns because members contribute the larger share of revenue.",
    "- Schedule stronger staffing and promotions around peak sales hours.",
    "- Compare lower-performing product lines with top categories for pricing, promotion and assortment improvements.",
    "- Tailor branch-level campaigns to local performance rather than using one strategy for every store.",
]
REPORT.write_text("\n".join(lines), encoding="utf-8")
print(REPORT)
