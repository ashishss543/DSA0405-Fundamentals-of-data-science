# Experiment 6: Customer Purchase Analysis
# Description: Load grocery store sales data using Pandas, calculate total sales sum,
#              apply a 10% discount followed by an 18% tax, and output final total.

import pandas as pd

# Load store data
df = pd.read_csv("grocerystore.csv")

# Compute total sales
total_sales = df["Sales"].sum()
print("Total sales for the grocery store:", round(total_sales, 2))

# Tax & discount parameters
discount = 0.10
tax = 0.18

# Apply discount and tax calculations
price_after_discount = total_sales - (total_sales * discount)
price_after_tax = price_after_discount + (price_after_discount * tax)

# Output final calculated amount
print("Final amount after applying discount and tax:", round(price_after_tax, 2))
