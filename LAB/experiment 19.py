# Experiment 19: Sales and Profit Analysis
# Description: Load sales_data.csv using Pandas, calculate Total Sales per transaction,
#              compute total sales and overall profit (with 20% profit margin),
#              and display the top 5 most profitable products.

import pandas as pd

# a) Load sales_data.csv into DataFrame
df = pd.read_csv("Sales_data.csv")

# b) Create 'Total Sales' column: Quantity Sold * Unit Price
df["Total Sales"] = df["Quantity Sold"] * df["Unit Price"]

# c) Calculate total sales for each product
product_sales = df.groupby("Product")["Total Sales"].sum().reset_index()

# Consider a 20% profit margin
profit_margin = 0.20
product_sales["Profit"] = product_sales["Total Sales"] * profit_margin

# Total overall profit
total_profit = product_sales["Profit"].sum()

# Top 5 most profitable products
top_5_profitable = product_sales.sort_values(by="Profit", ascending=False).head(5)

# Display results
print("Sales Data with Total Sales Column:")
print(df[["Date", "Product", "Quantity Sold", "Unit Price", "Total Sales"]])

print("\n" + "=" * 50)
print("Total Sales & Profit by Product (20% Profit Margin):")
print("=" * 50)
print(product_sales.to_string(index=False))

print(f"\nOverall Total Profit: ${total_profit:.2f}")

print("\n" + "=" * 50)
print("Top 5 Most Profitable Products:")
print("=" * 50)
print(top_5_profitable.to_string(index=False))
