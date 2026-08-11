# Experiment 10: Monthly Sales Visualization
# Description: Load sales data using Pandas, aggregate total sales per month,
#              and visualize monthly sales data using line plot and bar chart via Matplotlib.

import pandas as pd
import matplotlib.pyplot as plt

# Load sales dataset
df = pd.read_csv('Sales_data.csv')

# Calculate monthly total sales
monthly_sales = df.groupby("Month_sales")["Price"].sum()

# Display summary
print("Monthly Sales Data:\n", monthly_sales)

# 1. Line Plot
plt.figure(figsize=(8, 5))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o')
plt.title("Monthly Sales Data")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=60)
plt.tight_layout()
plt.savefig("outputs/experiment 10_line_plot.png")
plt.show()

# 2. Bar Chart
plt.figure(figsize=(8, 5))
plt.bar(monthly_sales.index, monthly_sales.values)
plt.title("Monthly Sales Data")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=60)
plt.tight_layout()
plt.savefig("outputs/experiment 10_bar_chart.png")
plt.show()
