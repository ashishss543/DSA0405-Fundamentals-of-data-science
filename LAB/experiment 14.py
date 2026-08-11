# Experiment 14: Frequency Distribution of Customer Ages
# Description: Load customer purchase dataset using Pandas and determine the frequency distribution
#              and relative distribution of customer ages.

import pandas as pd

# Load customer purchase dataset
df = pd.read_csv("customer_purchases.csv")

# Compute frequency distribution of customer ages
age_frequency = df["Age"].value_counts().sort_index()
age_percentage = df["Age"].value_counts(normalize=True).sort_index() * 100

# Summary DataFrame
age_distribution_df = pd.DataFrame({
    "Count": age_frequency,
    "Percentage (%)": age_percentage.round(2)
})

# Display outputs
print("Frequency Distribution of Customer Ages:")
print(age_distribution_df)
print("\nDescriptive Statistics of Customer Ages:")
print(df["Age"].describe())
