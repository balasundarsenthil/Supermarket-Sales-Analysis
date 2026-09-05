# Power BI Dashboard Plan

## Data Model
Import `data/cleaned_supermarket_sales.csv` into Power BI as `Sales`.

Create a Date table if needed:
```DAX
DateTable =
ADDCOLUMNS(
    CALENDAR(MIN(Sales[Date]), MAX(Sales[Date])),
    "Year", YEAR([Date]),
    "Month Number", MONTH([Date]),
    "Month", FORMAT([Date], "MMM"),
    "Day", DAY([Date]),
    "Day Name", FORMAT([Date], "DDD")
)
```

Relate `DateTable[Date]` to `Sales[Date]`.

## Core Measures
```DAX
Total Sales = SUM(Sales[Sales])

Total Profit = SUM(Sales[gross income])

Total Quantity = SUM(Sales[Quantity])

Total Transactions = DISTINCTCOUNT(Sales[Invoice ID])

Average Transaction Value = DIVIDE([Total Sales], [Total Transactions])

Profit Margin % = DIVIDE([Total Profit], [Total Sales])

Average Rating = AVERAGE(Sales[Rating])

Previous Month Sales =
CALCULATE(
    [Total Sales],
    DATEADD(DateTable[Date], -1, MONTH)
)

Sales Growth % =
DIVIDE(
    [Total Sales] - [Previous Month Sales],
    [Previous Month Sales]
)
```

## Page 1 — Executive Overview
KPI cards:
- Total Sales
- Total Profit
- Total Transactions
- Average Transaction Value
- Total Quantity

Charts:
- Monthly Sales Trend
- Sales by Product Line
- Sales by Branch
- Sales by Customer Type
- Sales by Payment

Slicers:
- Date
- Branch
- Product line
- Gender
- Customer type
- Payment

## Page 2 — Product Performance
- Revenue by Product Line
- Profit by Product Line
- Quantity Sold
- Product-line ranking
- Revenue/profit comparison

## Page 3 — Customer Analysis
- Member vs Normal revenue
- Gender revenue
- Average transaction value by customer type
- Transaction count by customer type
- Gender/customer-type matrix

## Page 4 — Branch Performance
- Revenue by branch
- Profit by branch
- Transactions by branch
- Average transaction value
- Branch x Product Line matrix/heatmap

## Page 5 — Time & Sales Trends
- Daily revenue trend
- Monthly revenue trend
- Day-of-week revenue
- Hourly revenue
- Peak sales hour

## Interaction Features
- Cross-filtering
- Drill-through from branch/product visuals
- Report-page tooltips
- Conditional formatting
- Dynamic chart titles
- Reset filters/bookmark button
