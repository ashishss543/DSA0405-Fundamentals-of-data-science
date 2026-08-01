import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 1. GENERATE RAW MOCK DATA (Simulating an imperfect CSV file)
raw_data = {
    "Employee_Name": [" Alice ", "Bob", "Charlie", "Diana", "Evan"],
    "Department": ["HR", "Engineering", "HR", "Engineering", "Marketing"],
    "Salary": [50000, 85000, np.nan, 92000, 60000],  # Missing value
    "Join_Date": [
        "2022-01-15",
        "2021-06-20",
        "2023-03-11",
        "2020-11-01",
        "2024-02-28",
    ],
}
df = pd.DataFrame(raw_data)
print("--- Raw Data ---")
print(df, "\n")

# 2. DATA PREPROCESSING
# Clean whitespace from text strings
df["Employee_Name"] = df["Employee_Name"].str.strip()

# Handle missing values by replacing NaN with the median salary
median_salary = df["Salary"].median()
df["Salary"] = df["Salary"].fillna(median_salary)

# Convert string dates into proper datetime format
df["Join_Date"] = pd.to_datetime(df["Join_Date"])

# Create a calculated feature (Years of service based on current year 2026)
df["Years_of_Service"] = 2026 - df["Join_Date"].dt.year
print("--- Preprocessed Data ---")
print(df, "\n")

# 3. DATA AGGREGATION
# Group by department and compute average metrics
dept_summary = (
    df.groupby("Department")
    .agg(Avg_Salary=("Salary", "mean"), Total_Employees=("Employee_Name", "count"))
    .reset_index()
)
print("--- Aggregated Summary ---")
print(dept_summary, "\n")

# 4. DATA VISUALIZATION
# Set visual style theme
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1: Bar chart of average salaries across departments
sns.barplot(
    data=dept_summary,
    x="Department",
    y="Avg_Salary",
    hue="Department",
    ax=axes[0],
    palette="Blues_d",
    legend=False,
)
axes[0].set_title("Average Salary by Department")
axes[0].set_xlabel("Department")
axes[0].set_ylabel("Salary ($)")

# Plot 2: Scatter plot mapping experience against compensation
sns.scatterplot(
    data=df,
    x="Years_of_Service",
    y="Salary",
    hue="Department",
    style="Department",
    s=200,
    ax=axes[1],
)
axes[1].set_title("Salary vs. Years of Service")
axes[1].set_xlabel("Years of Service")
axes[1].set_ylabel("Salary ($)")

plt.tight_layout()
plt.savefig("salary_analysis_plot.png")
print("Plot saved successfully as 'salary_analysis_plot.png'")
# Non-blocking or comment out plt.show() for script execution
# plt.show()
