# Experiment 2: Past Month Price Average
# Description: Load sales dataset using Pandas and compute the average price for November 2023 sales.

import pandas as pd

# Load sales data
df = pd.read_csv("Sales_data.csv")

# Filter for November 2023 and compute mean price
average_price = df[df["Month_sales"] == "November 2023"]["Price"].mean()

# Output result
print("Average price in November 2023 (Past Month):", round(average_price, 2))
