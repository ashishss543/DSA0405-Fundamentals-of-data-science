# Experiment 5: Fuel Efficiency Analysis
# Description: Load vehicle fuel data using NumPy, calculate overall average fuel efficiency,
#              compare average MPG for Mazda vs Audi, and calculate percentage improvement.

import numpy as np

# Load dataset using genfromtxt
fuel_data = np.genfromtxt('Fuel_data.csv', delimiter=',', skip_header=1, dtype=str)

fuel_efficiency = fuel_data[:, 7].astype(float)
make = fuel_data[:, 8]

# Calculate overall average efficiency
average_efficiency = np.mean(fuel_efficiency)

# Calculate brand-specific average efficiencies
mazda_eff = fuel_efficiency[make == "mazda"]
audi_eff = fuel_efficiency[make == "audi"]

mazda_avg = np.mean(mazda_eff)
audi_avg = np.mean(audi_eff)

# Compute percentage improvement from Mazda to Audi
percentage_improvement = ((mazda_avg - audi_avg) / audi_avg) * 100

# Output results
print("Average Fuel Efficiency of all cars:", round(average_efficiency, 2), "MPG")
print("Average Fuel Efficiency of Mazda:", round(mazda_avg, 2), "MPG")
print("Average Fuel Efficiency of Audi:", round(audi_avg, 2), "MPG")
print("Percentage Improvement from Mazda to Audi:", round(percentage_improvement, 2), "%")
