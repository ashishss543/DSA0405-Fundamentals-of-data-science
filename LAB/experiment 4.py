# Experiment 4: Quarterly Sales Analysis using NumPy
# Description: Analyze sales dataset to compute Q1 (Jan-Mar) and Q4 (Oct-Dec) sales, 
#              total yearly sales, and percentage increase from Q1 to Q4 using NumPy.

import numpy as np

# Load raw text matrix skipping header
sales_data = np.genfromtxt("Sales_data.csv", delimiter=",", skip_header=1, dtype=str)

months = sales_data[:, 1]
sales = sales_data[:, 4].astype(float)

Q1 = 0.0
Q4 = 0.0

# Calculate sales sums for Q1 and Q4
for i in range(len(months)):
    if ("January" in months[i]) or ("February" in months[i]) or ("March" in months[i]):
        Q1 += sales[i]
    elif ("October" in months[i]) or ("November" in months[i]) or ("December" in months[i]):
        Q4 += sales[i]

# Compute overall total sales and growth percentage
total_sales_year = np.sum(sales)
percentage_increase = ((Q4 - Q1) / Q1) * 100

# Output results
print("Total sales for the year:", round(total_sales_year, 2))
print("Percentage increase from Q1 to Q4:", round(percentage_increase, 2), "%")
