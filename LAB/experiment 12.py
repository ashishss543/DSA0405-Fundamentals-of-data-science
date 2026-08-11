# Experiment 12: Temperature and Rainfall Visualization
# Description: Load monthly temperature and rainfall dataset using Pandas,
#              generate a line plot for temperature and a scatter plot for rainfall using Matplotlib.

import pandas as pd
import matplotlib.pyplot as plt

# Load temperature and rainfall dataset
df = pd.read_csv("temperature_rainfall.csv")

print("Monthly Weather Data:")
print(df)

# 1. Line Plot of Monthly Temperature
plt.figure(figsize=(9, 5))
plt.plot(df["Month"], df["Temperature"], marker='o', color='crimson', linewidth=2, label="Temperature (°C)")
plt.title("Monthly Temperature Trend (Line Plot)")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("outputs/experiment 12_temperature_line_plot.png")
plt.close()

# 2. Scatter Plot of Monthly Rainfall
plt.figure(figsize=(9, 5))
plt.scatter(df["Month"], df["Rainfall"], color='dodgerblue', s=100, label="Rainfall (mm)")
plt.title("Monthly Rainfall Distribution (Scatter Plot)")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("outputs/experiment 12_rainfall_scatter_plot.png")
plt.close()

print("\nTemperature line plot and rainfall scatter plot generated and saved in outputs folder.")
