# Experiment 20: Customer Segmentation Analysis
# Description: Load customer_data.csv using Pandas, segment customers into Low, Medium, 
#              and High Spenders based on Total Spending, and compute the average age per segment.

import pandas as pd

# a) Load customer_data.csv into DataFrame
df = pd.read_csv("customer_data.csv")

# b) Segment customers into three groups: Low, Medium, and High Spenders
df["Spending Segment"] = pd.qcut(
    df["Total Spending"], 
    q=3, 
    labels=["Low Spenders", "Medium Spenders", "High Spenders"]
)

# c) Calculate average age of customers in each spending segment
avg_age_per_segment = df.groupby("Spending Segment", observed=False)["Age"].mean().reset_index()
avg_age_per_segment.rename(columns={"Age": "Average Age"}, inplace=True)

# Display results
print("Customer Data with Spending Segments:")
print(df[["Customer ID", "Age", "Gender", "Total Spending", "Spending Segment"]].to_string(index=False))

print("\n" + "=" * 45)
print("Average Age of Customers by Spending Segment:")
print("=" * 45)
print(avg_age_per_segment.to_string(index=False))

# Additional summary by gender & segment
segment_summary = df.groupby("Spending Segment", observed=False).agg(
    Customer_Count=("Customer ID", "count"),
    Average_Age=("Age", "mean"),
    Average_Spending=("Total Spending", "mean")
).reset_index()

print("\n" + "=" * 65)
print("Comprehensive Spending Segment Summary:")
print("=" * 65)
print(segment_summary.to_string(index=False))
