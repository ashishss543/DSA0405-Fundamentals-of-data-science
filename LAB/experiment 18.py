# Experiment 18: Statistical Analysis & Visualization of Age and Body Fat
# Description: Compute mean, median, standard deviation for Age and %Fat using Pandas,
#              and generate Boxplots, Scatter Plot, and Q-Q Plots using Matplotlib and SciPy.

import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

# Load or define dataset
data = {
    "age": [23, 23, 27, 27, 39, 41, 47, 49, 50, 52, 54, 54, 56, 57, 58, 58, 60, 61],
    "%fat": [9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2, 34.6, 42.5, 28.8, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7]
}
df = pd.DataFrame(data)

# 1. Statistical Calculations
mean_age = df["age"].mean()
median_age = df["age"].median()
std_age = df["age"].std()

mean_fat = df["%fat"].mean()
median_fat = df["%fat"].median()
std_fat = df["%fat"].std()

print("Statistical Summary for Age and %Fat:")
print("=" * 45)
print(f"Age   -> Mean: {mean_age:.2f}, Median: {median_age:.2f}, Std Dev: {std_age:.2f}")
print(f"%Fat  -> Mean: {mean_fat:.2f}, Median: {median_fat:.2f}, Std Dev: {std_fat:.2f}")
print("=" * 45)

# 2. Boxplots for Age and %Fat
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].boxplot(df["age"], patch_artist=True, boxprops=dict(facecolor='lightblue'))
axes[0].set_title("Boxplot of Age")
axes[0].set_ylabel("Age (years)")

axes[1].boxplot(df["%fat"], patch_artist=True, boxprops=dict(facecolor='lightgreen'))
axes[1].set_title("Boxplot of %Fat")
axes[1].set_ylabel("% Body Fat")

plt.tight_layout()
plt.savefig("outputs/experiment 18_boxplots.png")
plt.close()

# 3. Scatter Plot of Age vs %Fat
plt.figure(figsize=(8, 5))
plt.scatter(df["age"], df["%fat"], color='darkorange', edgecolors='black', s=80)
plt.title("Scatter Plot: Age vs %Fat")
plt.xlabel("Age (years)")
plt.ylabel("% Body Fat")
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("outputs/experiment 18_scatter.png")
plt.close()

# 4. Q-Q Plots for Age and %Fat
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
stats.probplot(df["age"], dist="norm", plot=axes[0])
axes[0].set_title("Q-Q Plot for Age")

stats.probplot(df["%fat"], dist="norm", plot=axes[1])
axes[1].set_title("Q-Q Plot for %Fat")

plt.tight_layout()
plt.savefig("outputs/experiment 18_qqplot.png")
plt.close()

print("\nVisualizations saved to outputs folder: Boxplots, Scatter Plot, and Q-Q Plots.")
