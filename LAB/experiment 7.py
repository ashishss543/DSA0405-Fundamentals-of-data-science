# Experiment 7: Customer Order Analysis
# Description: Read order data using Pandas, aggregate total orders per customer, 
#              compute average order total per product item, and retrieve min/max order dates.

import pandas as pd

# Load order dataset
df = pd.read_csv("order_data.csv")

# Aggregations
total_orders = df.groupby("Full Name")["Order Count"].sum()
avg_order_per_product = df.groupby("Items")["Order Total"].mean()
earliest_order = df["Order"].min()
latest_order = df["Order"].max()

# Display outputs
print("Total number of orders made by each customer:\n", total_orders)
print("Average order quantity for each product:\n", avg_order_per_product)
print("Earliest order date:", earliest_order)
print("Latest order date:", latest_order)
