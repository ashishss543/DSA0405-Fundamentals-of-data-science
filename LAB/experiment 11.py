# Experiment 11: Product Sales Visualization
# Description: Visualize monthly sales data of products using Matplotlib 
#              (Line Plot, Scatter Plot, and Bar Plot).

import matplotlib.pyplot as plt

# Monthly Sales Data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sales = [12000, 15000, 14000, 18000, 22000, 26000, 24000, 28000, 31000, 29000, 35000, 42000]

print("Monthly Sales Data:")
for m, s in zip(months, sales):
    print(f"{m}: ${s}")

# 1. Line Plot
plt.figure(figsize=(8, 5))
plt.plot(months, sales, marker='o', color='blue', linestyle='-', linewidth=2)
plt.title("Monthly Product Sales (Line Plot)")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.grid(True)
plt.tight_layout()
plt.savefig("outputs/experiment 11_line_plot.png")
plt.close()

# 2. Scatter Plot
plt.figure(figsize=(8, 5))
plt.scatter(months, sales, color='red', s=80)
plt.title("Monthly Product Sales (Scatter Plot)")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.grid(True)
plt.tight_layout()
plt.savefig("outputs/experiment 11_scatter_plot.png")
plt.close()

# 3. Bar Plot
plt.figure(figsize=(8, 5))
plt.bar(months, sales, color='teal', edgecolor='black')
plt.title("Monthly Product Sales (Bar Plot)")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.grid(axis='y')
plt.tight_layout()
plt.savefig("outputs/experiment 11_bar_plot.png")
plt.close()

print("\nPlots saved to outputs folder: Line Plot, Scatter Plot, and Bar Plot.")
