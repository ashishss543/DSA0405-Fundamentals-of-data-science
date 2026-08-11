"""
Download Datasets for Descriptive Statistics Assessment
Downloads CSV datasets from public GitHub/URL sources for each question.
"""

import os
import urllib.request
import pandas as pd
import numpy as np

BASE_DIR = r"c:\LABS\FDS-LAB\Assesment Tool\Hands on descriptive statics"
DATASETS_DIR = os.path.join(BASE_DIR, "datasets")
os.makedirs(DATASETS_DIR, exist_ok=True)

print("=" * 60)
print("  DOWNLOADING DATASETS FOR DESCRIPTIVE STATISTICS LAB")
print("=" * 60)

# Q1: Employee Dataset
print("\n[Q1] Creating Employee Dataset...")
np.random.seed(42)
n = 200
depts = ["HR", "IT", "Finance", "Marketing", "Operations"]
employee_data = {
    "EmployeeID": range(1001, 1001 + n),
    "Name": [f"Employee_{i}" for i in range(1, n + 1)],
    "Age": np.random.randint(22, 60, n),
    "Department": np.random.choice(depts, n),
    "Salary": np.round(np.random.normal(55000, 15000, n), 2),
    "YearsExperience": np.random.randint(0, 35, n),
    "PerformanceScore": np.random.choice([1, 2, 3, 4, 5], n),
    "Gender": np.random.choice(["Male", "Female"], n),
    "HoursPerWeek": np.random.randint(35, 60, n),
    "Training": np.random.choice([True, False], n),
}
df_employee = pd.DataFrame(employee_data)
for col in ["Age", "Salary", "PerformanceScore", "HoursPerWeek"]:
    idx = np.random.choice(df_employee.index, size=int(n * 0.05), replace=False)
    df_employee.loc[idx, col] = np.nan
df_employee.to_csv(os.path.join(DATASETS_DIR, "employee_dataset.csv"), index=False)
print(f"   Saved: employee_dataset.csv ({len(df_employee)} rows)")

# Q2: Student Grades Dataset
print("\n[Q2] Creating Student Grades Dataset...")
grades = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "F"]
weights = [0.05, 0.10, 0.08, 0.12, 0.15, 0.10, 0.12, 0.10, 0.07, 0.07, 0.04]
n_students = 300
student_data = {
    "StudentID": range(1, n_students + 1),
    "Name": [f"Student_{i}" for i in range(1, n_students + 1)],
    "Grade": np.random.choice(grades, n_students, p=weights),
    "Score": np.round(np.random.normal(68, 15, n_students).clip(0, 100), 1),
    "Subject": np.random.choice(["Math", "Science", "English", "History", "CS"], n_students),
    "Semester": np.random.choice(["Spring 2024", "Fall 2024", "Spring 2025"], n_students),
}
df_students = pd.DataFrame(student_data)
df_students.to_csv(os.path.join(DATASETS_DIR, "student_grades.csv"), index=False)
print(f"   Saved: student_grades.csv ({len(df_students)} rows)")

# Q3: House Prices Dataset
print("\n[Q3] Downloading House Prices Dataset...")
house_url = "https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv"
path_house = os.path.join(DATASETS_DIR, "house_prices.csv")
try:
    urllib.request.urlretrieve(house_url, path_house)
    df_house = pd.read_csv(path_house)
    if "medv" in df_house.columns:
        df_house.rename(columns={"medv": "Price"}, inplace=True)
        df_house.to_csv(path_house, index=False)
    print(f"   Saved: house_prices.csv ({len(df_house)} rows)")
except Exception as e:
    print(f"   Download failed, generating synthetic: {e}")
    prices = np.concatenate([
        np.random.normal(250000, 60000, 350),
        np.random.normal(500000, 80000, 100),
        np.random.normal(120000, 20000, 50),
    ])
    prices = prices[prices > 0]
    df_house = pd.DataFrame({
        "Price": np.round(prices, 2),
        "Sqft": np.random.randint(800, 5000, len(prices)),
        "Bedrooms": np.random.randint(1, 7, len(prices)),
        "YearBuilt": np.random.randint(1950, 2024, len(prices)),
    })
    df_house.to_csv(path_house, index=False)
    print(f"   Saved: house_prices.csv ({len(df_house)} rows, synthetic)")

# Q4: Salary Dataset
print("\n[Q4] Creating Salary Dataset...")
np.random.seed(10)
roles = ["Junior", "Mid", "Senior", "Lead", "Manager", "Director", "VP", "C-Level"]
salaries, role_list = [], []
for r in roles:
    mean = {"Junior": 45000, "Mid": 65000, "Senior": 90000, "Lead": 105000,
            "Manager": 120000, "Director": 150000, "VP": 200000, "C-Level": 350000}[r]
    salaries.extend(np.random.normal(mean, mean * 0.15, 50).tolist())
    role_list.extend([r] * 50)
salaries.extend([8000, 9500, 7200, 750000, 900000, 1200000])
role_list.extend(["Junior", "Junior", "Junior", "C-Level", "C-Level", "C-Level"])
df_sal = pd.DataFrame({
    "Role": role_list,
    "Salary": np.round(salaries, 2),
    "Department": np.random.choice(["Tech", "Finance", "Marketing", "Ops"], len(role_list)),
    "Experience_Years": np.random.randint(0, 30, len(role_list)),
})
df_sal.to_csv(os.path.join(DATASETS_DIR, "salary_data.csv"), index=False)
print(f"   Saved: salary_data.csv ({len(df_sal)} rows)")

# Q5: Student Marks Dataset (IQR Outlier Detection)
print("\n[Q5] Creating Student Marks Dataset...")
np.random.seed(7)
n_m = 150
marks_data = {
    "StudentID": range(1, n_m + 1),
    "Math": np.clip(np.round(np.concatenate([np.random.normal(65, 12, 140), [5, 8, 98, 99, 100, 3, 97, 2, 101, 102]]), 1), 0, 105),
    "Science": np.clip(np.round(np.concatenate([np.random.normal(70, 10, 140), [4, 9, 97, 98, 99, 6, 100, 1, 103, 105]]), 1), 0, 105),
    "English": np.clip(np.round(np.concatenate([np.random.normal(60, 15, 140), [3, 7, 95, 97, 98, 5, 99, 0, 100, 101]]), 1), 0, 105),
}
df_marks = pd.DataFrame(marks_data)
df_marks.to_csv(os.path.join(DATASETS_DIR, "student_marks.csv"), index=False)
print(f"   Saved: student_marks.csv ({len(df_marks)} rows)")

# Q6: Sales Dataset (IQR Outlier Removal)
print("\n[Q6] Creating Sales Dataset...")
np.random.seed(99)
n_sales = 250
outlier_sales = [50000, 75000, 80000, 100, 50, 200, 120000, 85000, 90, 45000,
                 55000, 60000, 70000, 80, 130, 150, 95000, 110000, 115000, 70]
sales_data = {
    "SaleID": range(1, n_sales + 1),
    "Product": np.random.choice(["Laptop", "Phone", "Tablet", "Monitor", "Keyboard"], n_sales),
    "Region": np.random.choice(["North", "South", "East", "West"], n_sales),
    "SalesAmount": np.concatenate([np.random.normal(5000, 1200, 230), outlier_sales]),
    "Units": np.random.randint(1, 100, n_sales),
    "Discount": np.round(np.random.uniform(0, 0.4, n_sales), 2),
}
df_sales = pd.DataFrame(sales_data)
df_sales.to_csv(os.path.join(DATASETS_DIR, "sales_data.csv"), index=False)
print(f"   Saved: sales_data.csv ({len(df_sales)} rows)")

# Q7: Pollution Dataset (Before/After Outlier Visualization)
print("\n[Q7] Creating Pollution Dataset...")
np.random.seed(55)
n_poll = 200
out_pm = [400, 450, 500, 600, 700, 750, 1, 2, 3, 4, 5, 6, 7, 8, 9]
out_no2 = [300, 350, 400, 450, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
out_co = [10, 12, 15, 20, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10, 0.11]
poll_data = {
    "City": np.random.choice(["Delhi", "Mumbai", "Chennai", "Kolkata", "Bangalore"], n_poll),
    "PM2_5": np.concatenate([np.random.normal(80, 20, 185), out_pm]),
    "NO2": np.concatenate([np.random.normal(50, 10, 185), out_no2]),
    "CO": np.round(np.concatenate([np.random.normal(1.5, 0.4, 185), out_co]), 3),
    "Temperature": np.round(np.random.normal(28, 6, n_poll), 1),
    "Humidity": np.round(np.random.normal(65, 15, n_poll).clip(20, 100), 1),
}
df_poll = pd.DataFrame(poll_data)
df_poll.to_csv(os.path.join(DATASETS_DIR, "pollution_data.csv"), index=False)
print(f"   Saved: pollution_data.csv ({len(df_poll)} rows)")

# Q8: Titanic Dataset
print("\n[Q8] Downloading Titanic Dataset...")
titanic_url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
path_titanic = os.path.join(DATASETS_DIR, "titanic.csv")
try:
    urllib.request.urlretrieve(titanic_url, path_titanic)
    df_titanic = pd.read_csv(path_titanic)
    print(f"   Saved: titanic.csv ({len(df_titanic)} rows)")
except Exception as e:
    print(f"   Download failed, generating synthetic: {e}")
    n_t = 891
    titanic_data = {
        "PassengerId": range(1, n_t + 1),
        "Survived": np.random.choice([0, 1], n_t, p=[0.62, 0.38]),
        "Pclass": np.random.choice([1, 2, 3], n_t, p=[0.24, 0.21, 0.55]),
        "Name": [f"Person_{i}" for i in range(1, n_t + 1)],
        "Sex": np.random.choice(["male", "female"], n_t, p=[0.65, 0.35]),
        "Age": np.where(np.random.rand(n_t) > 0.2, np.round(np.random.normal(29, 14, n_t).clip(1, 80), 1), np.nan),
        "SibSp": np.random.choice([0, 1, 2, 3, 4], n_t, p=[0.68, 0.23, 0.06, 0.02, 0.01]),
        "Parch": np.random.choice([0, 1, 2, 3], n_t, p=[0.76, 0.13, 0.08, 0.03]),
        "Fare": np.round(np.random.lognormal(3.0, 1.0, n_t), 4),
        "Embarked": np.where(np.random.rand(n_t) > 0.05, np.random.choice(["S", "C", "Q"], n_t, p=[0.72, 0.19, 0.09]), np.nan),
    }
    df_titanic = pd.DataFrame(titanic_data)
    df_titanic.to_csv(path_titanic, index=False)
    print(f"   Saved: titanic.csv ({len(df_titanic)} rows, synthetic)")

print("\n" + "=" * 60)
print("  ALL DATASETS READY!")
print("=" * 60)
print(f"\n  Location: {DATASETS_DIR}")
for f in sorted(os.listdir(DATASETS_DIR)):
    fpath = os.path.join(DATASETS_DIR, f)
    size = os.path.getsize(fpath)
    print(f"    * {f}  ({size:,} bytes)")
