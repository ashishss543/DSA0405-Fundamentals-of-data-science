# Experiment 8: Top 5 Most Sold Products Analysis
# Description: Load sales data using Pandas, aggregate total sales per product, 
#              and identify the top 5 most sold products by total sales value.

import pandas as pd

# Load sales dataset
df = pd.read_csv("Sales_data.csv")

# Group by product name, sum price, and get top 5 products
top_5_products = df.groupby("Product_Name")["Price"].sum().nlargest(5)

# Output results
print("Five most sold products: ", top_5_products)
