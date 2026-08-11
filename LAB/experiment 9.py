# Experiment 9: House Data Analysis
# Description: Load housing dataset using Pandas, calculate average house price for each location,
#              count houses with more than 4 bedrooms, and find the largest house size.

import pandas as pd

# Load housing dataset
df = pd.read_csv("house.csv")

# Perform aggregations and filtering
location_price_average = df.groupby("Location")["price"].mean()
more_than_4beds = df[df["beds"] > 4].count()["beds"]
largest_sq_feet = df["size"].max()

# Output results
print("Average house price for each location: ", location_price_average)
print("Number of houses with more than 4 bedrooms: ", more_than_4beds)
print("Largest house size: ", largest_sq_feet)
