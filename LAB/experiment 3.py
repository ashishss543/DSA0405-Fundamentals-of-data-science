# Experiment 3: House Average Price Analysis
# Description: Load house market dataset with NumPy, filter houses with more than 4 bedrooms, 
#              and calculate their average price.

import numpy as np

# Load dataset skipping header row
house_data = np.loadtxt('House_data.csv', delimiter=',', skiprows=1)

# Filter houses where bedrooms count (column index 1) > 4
houses_more_than_4 = house_data[house_data[:, 1] > 4]

# Calculate mean price (column index 5) for filtered houses
average_price = np.mean(houses_more_than_4[:, 5])

# Output result
print("Average price of houses with more than 4 bedrooms:", round(average_price, 2))
