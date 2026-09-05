-- Supermarket Sales Analysis
-- MySQL 8+
-- Import cleaned_supermarket_sales.csv into a table named supermarket_sales.

CREATE DATABASE IF NOT EXISTS supermarket_db;
USE supermarket_db;

-- Recommended table structure
CREATE TABLE IF NOT EXISTS supermarket_sales (
    invoice_id VARCHAR(30),
    branch VARCHAR(20),
    city VARCHAR(50),
    customer_type VARCHAR(20),
    gender VARCHAR(20),
    product_line VARCHAR(100),
    unit_price DECIMAL(10,2),
    quantity INT,
    tax_5 DECIMAL(12,4),
    sales DECIMAL(12,4),
    sale_date DATE,
    sale_time TIME,
    payment VARCHAR(30),
    cogs DECIMAL(12,4),
    gross_margin_percentage DECIMAL(10,6),
    gross_income DECIMAL(12,4),
    rating DECIMAL(4,2),
    year INT,
    month INT,
    month_name VARCHAR(20),
    day INT,
    day_of_week VARCHAR(20),
    hour INT
);

-- 1. Overall KPIs
SELECT
    SUM(sales) AS total_revenue,
    SUM(gross_income) AS total_profit,
    COUNT(DISTINCT invoice_id) AS total_transactions,
    SUM(quantity) AS total_quantity,
    AVG(sales) AS average_transaction_value
FROM supermarket_sales;

-- 2. Sales by branch
SELECT branch, SUM(sales) AS revenue, SUM(gross_income) AS profit,
       COUNT(DISTINCT invoice_id) AS transactions
FROM supermarket_sales
GROUP BY branch
ORDER BY revenue DESC;

-- 3. Product-line performance
SELECT product_line, SUM(sales) AS revenue, SUM(gross_income) AS profit,
       SUM(quantity) AS quantity_sold
FROM supermarket_sales
GROUP BY product_line
ORDER BY revenue DESC;

-- 4. Customer type
SELECT customer_type, SUM(sales) AS revenue,
       COUNT(DISTINCT invoice_id) AS transactions,
       AVG(sales) AS avg_transaction
FROM supermarket_sales
GROUP BY customer_type
ORDER BY revenue DESC;

-- 5. Gender analysis
SELECT gender, SUM(sales) AS revenue,
       COUNT(DISTINCT invoice_id) AS transactions,
       AVG(sales) AS avg_transaction
FROM supermarket_sales
GROUP BY gender
ORDER BY revenue DESC;

-- 6. Payment analysis
SELECT payment, COUNT(DISTINCT invoice_id) AS transactions,
       SUM(sales) AS revenue
FROM supermarket_sales
GROUP BY payment
ORDER BY revenue DESC;

-- 7. Monthly sales
SELECT year, month, month_name, SUM(sales) AS revenue
FROM supermarket_sales
GROUP BY year, month, month_name
ORDER BY year, month;

-- 8. Day-of-week performance
SELECT day_of_week, SUM(sales) AS revenue,
       COUNT(DISTINCT invoice_id) AS transactions
FROM supermarket_sales
GROUP BY day_of_week
ORDER BY revenue DESC;

-- 9. Hourly performance
SELECT hour, SUM(sales) AS revenue,
       COUNT(DISTINCT invoice_id) AS transactions
FROM supermarket_sales
GROUP BY hour
ORDER BY revenue DESC;

-- 10. Branch x Product Line
SELECT branch, product_line,
       SUM(sales) AS revenue,
       SUM(gross_income) AS profit
FROM supermarket_sales
GROUP BY branch, product_line
ORDER BY branch, revenue DESC;

-- 11. Top 10 transactions
SELECT invoice_id, branch, product_line, sales, gross_income
FROM supermarket_sales
ORDER BY sales DESC
LIMIT 10;

-- 12. Profit margin KPI
SELECT
    SUM(gross_income) / NULLIF(SUM(sales), 0) * 100 AS gross_profit_margin_pct
FROM supermarket_sales;
