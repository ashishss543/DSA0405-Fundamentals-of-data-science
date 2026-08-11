"""
============================================================
  DESCRIPTIVE STATISTICS - HANDS-ON ASSESSMENT
  Unit 3 | All 8 Questions | Python Solutions
============================================================
"""

import os
import sys
import warnings
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend for saving files
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns
from scipy import stats

warnings.filterwarnings("ignore")

# ─── Paths ───────────────────────────────────────────────
BASE_DIR    = r"c:\LABS\FDS-LAB\Assesment Tool\Hands on descriptive statics"
DATASETS    = os.path.join(BASE_DIR, "datasets")
OUTPUTS     = os.path.join(BASE_DIR, "outputs")
os.makedirs(OUTPUTS, exist_ok=True)
import io

# -------------------------------------------------------
# Save all console output to a text file
# -------------------------------------------------------

log_file = os.path.join(OUTPUTS, "Complete_Output_Report.txt")

class Tee:
    def __init__(self, *files):
        self.files = files

    def write(self, obj):
        for f in self.files:
            f.write(obj)
            f.flush()

    def flush(self):
        for f in self.files:
            f.flush()

log = open(log_file, "w", encoding="utf-8")

# Print both to console and text file
sys.stdout = Tee(sys.__stdout__, log)

# ─── Style ───────────────────────────────────────────────
plt.rcParams.update({
    "figure.facecolor": "#0d1117",
    "axes.facecolor":   "#161b22",
    "axes.edgecolor":   "#30363d",
    "axes.labelcolor":  "#e6edf3",
    "axes.titlecolor":  "#e6edf3",
    "axes.titlesize":   14,
    "axes.labelsize":   12,
    "text.color":       "#e6edf3",
    "xtick.color":      "#8b949e",
    "ytick.color":      "#8b949e",
    "grid.color":       "#21262d",
    "grid.linestyle":   "--",
    "grid.alpha":       0.7,
    "legend.facecolor": "#161b22",
    "legend.edgecolor": "#30363d",
    "legend.fontsize":  10,
    "figure.titlesize": 16,
    "figure.titleweight": "bold",
})

PALETTE    = ["#58a6ff", "#3fb950", "#f78166", "#d2a8ff", "#ffa657",
              "#39d353", "#ff7b72", "#79c0ff", "#a5d6ff", "#56d364"]
ACCENT     = "#58a6ff"
SUCCESS    = "#3fb950"
WARNING    = "#ffa657"
DANGER     = "#f78166"

def sep(n=1):
    """Print blank separator lines."""
    for _ in range(n):
        print()

def banner(title, q_num):
    print("\n" + "=" * 70)
    print(f"  Q{q_num}: {title}")
    print("=" * 70)

def save_fig(name):
    path = os.path.join(OUTPUTS, name)
    plt.savefig(path, dpi=150, bbox_inches="tight", facecolor=plt.gcf().get_facecolor())
    plt.close()
    print(f"  [Saved] outputs/{name}")
    return path


# ╔══════════════════════════════════════════════════════════════╗
# ║  Q1 – Employee Dataset Summary                               ║
# ╚══════════════════════════════════════════════════════════════╝
banner("Employee Dataset – Complete Summary", 1)

df = pd.read_csv(os.path.join(DATASETS, "employee_dataset.csv"))

print("\n--- 1. Number of Rows and Columns ---")
print(f"  Rows    : {df.shape[0]}")
print(f"  Columns : {df.shape[1]}")

print("\n--- 2. Column Data Types ---")
print(df.dtypes.to_string())

print("\n--- 3. Missing Values ---")
missing = df.isnull().sum()
missing_pct = (missing / len(df) * 100).round(2)
missing_df = pd.DataFrame({"Missing Count": missing, "Missing %": missing_pct})
print(missing_df[missing_df["Missing Count"] > 0].to_string())

print("\n--- 4. Statistical Summary (Numerical Columns) ---")
print(df.describe().round(2).to_string())

print("\n--- 5. Statistical Summary (Categorical Columns) ---")
print(df.describe(include="object").to_string())

# Visual summary
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle("Q1 – Employee Dataset Summary", color="#e6edf3", fontsize=18)

# Missing values heatmap
ax = axes[0, 0]
miss_heat = df.isnull().astype(int)
im = ax.imshow(miss_heat.T, aspect="auto", cmap="RdYlGn_r", vmin=0, vmax=1)
ax.set_yticks(range(len(df.columns)))
ax.set_yticklabels(df.columns, fontsize=9)
ax.set_xlabel("Row Index")
ax.set_title("Missing Values Heatmap")
plt.colorbar(im, ax=ax, label="Missing (1)")

# Missing values bar
ax = axes[0, 1]
miss_only = missing[missing > 0]
bars = ax.bar(miss_only.index, miss_only.values, color=DANGER, alpha=0.85, edgecolor="#21262d")
ax.set_title("Missing Value Counts")
ax.set_ylabel("Count")
for bar in bars:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
            str(int(bar.get_height())), ha="center", va="bottom", fontsize=10, color="#e6edf3")

# Department distribution
ax = axes[0, 2]
dept_counts = df["Department"].value_counts()
wedges, texts, autotexts = ax.pie(dept_counts, labels=dept_counts.index,
                                   autopct="%1.1f%%", colors=PALETTE[:len(dept_counts)],
                                   startangle=140, textprops={"color": "#e6edf3", "fontsize": 9})
ax.set_facecolor("#0d1117")
ax.set_title("Department Distribution")

# Salary distribution
ax = axes[1, 0]
sal_data = df["Salary"].dropna()
ax.hist(sal_data, bins=25, color=ACCENT, alpha=0.85, edgecolor="#21262d")
ax.axvline(sal_data.mean(), color=SUCCESS, linestyle="--", linewidth=2, label=f"Mean: {sal_data.mean():.0f}")
ax.axvline(sal_data.median(), color=WARNING, linestyle="--", linewidth=2, label=f"Median: {sal_data.median():.0f}")
ax.set_title("Salary Distribution")
ax.set_xlabel("Salary ($)")
ax.set_ylabel("Frequency")
ax.legend()

# Age distribution
ax = axes[1, 1]
ax.hist(df["Age"].dropna(), bins=20, color=PALETTE[3], alpha=0.85, edgecolor="#21262d")
ax.set_title("Age Distribution")
ax.set_xlabel("Age")
ax.set_ylabel("Frequency")

# Performance score
ax = axes[1, 2]
perf = df["PerformanceScore"].dropna().value_counts().sort_index()
ax.bar(perf.index.astype(str), perf.values, color=PALETTE[:len(perf)], edgecolor="#21262d", alpha=0.85)
ax.set_title("Performance Score Distribution")
ax.set_xlabel("Score")
ax.set_ylabel("Count")

plt.tight_layout()
save_fig("Q1_employee_summary.png")

# Save summary report
summary_path = os.path.join(OUTPUTS, "Q1_employee_summary_report.txt")
with open(summary_path, "w", encoding="utf-8") as f:
    f.write("Q1 – EMPLOYEE DATASET SUMMARY REPORT\n")
    f.write("=" * 60 + "\n\n")
    f.write(f"Shape: {df.shape[0]} rows x {df.shape[1]} columns\n\n")
    f.write("Data Types:\n")
    f.write(df.dtypes.to_string() + "\n\n")
    f.write("Missing Values:\n")
    f.write(missing_df.to_string() + "\n\n")
    f.write("Statistical Summary:\n")
    f.write(df.describe().round(2).to_string() + "\n")
print("  [Saved] outputs/Q1_employee_summary_report.txt")


# ╔══════════════════════════════════════════════════════════════╗
# ║  Q2 – Student Grades Frequency Distribution                  ║
# ╚══════════════════════════════════════════════════════════════╝
banner("Student Grades – Frequency Distribution & Bar Chart", 2)

df2 = pd.read_csv(os.path.join(DATASETS, "student_grades.csv"))

grade_order = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "F"]
freq = df2["Grade"].value_counts().reindex(grade_order).fillna(0).astype(int)
rel_freq = (freq / freq.sum() * 100).round(2)

print("\n--- Frequency Distribution Table ---")
freq_table = pd.DataFrame({
    "Grade": freq.index,
    "Frequency": freq.values,
    "Relative Frequency (%)": rel_freq.values,
    "Cumulative Frequency": freq.values.cumsum(),
})
print(freq_table.to_string(index=False))

# Plot
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
fig.suptitle("Q2 – Student Grades Frequency Distribution", fontsize=18)

# Bar chart
ax = axes[0]
colors_g = plt.cm.RdYlGn(np.linspace(0.9, 0.1, len(grade_order)))
bars = ax.bar(freq.index, freq.values, color=colors_g, edgecolor="#21262d", width=0.7)
ax.set_title("Grade Frequency – Bar Chart")
ax.set_xlabel("Grade")
ax.set_ylabel("Frequency")
ax.set_xticklabels(freq.index, rotation=45)
for bar in bars:
    if bar.get_height() > 0:
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
                str(int(bar.get_height())), ha="center", va="bottom", fontsize=9)

# Relative frequency
ax = axes[1]
ax.bar(rel_freq.index, rel_freq.values, color=colors_g, edgecolor="#21262d", width=0.7)
ax.set_title("Relative Frequency (%)")
ax.set_xlabel("Grade")
ax.set_ylabel("Percentage (%)")
ax.set_xticklabels(rel_freq.index, rotation=45)

# Cumulative frequency
ax = axes[2]
cum = freq.values.cumsum()
ax.plot(freq.index, cum, "o-", color=ACCENT, linewidth=2, markersize=7)
ax.fill_between(range(len(freq.index)), cum, alpha=0.25, color=ACCENT)
ax.set_xticks(range(len(freq.index)))
ax.set_xticklabels(freq.index, rotation=45)
ax.set_title("Cumulative Frequency")
ax.set_xlabel("Grade")
ax.set_ylabel("Cumulative Count")

plt.tight_layout()
save_fig("Q2_grade_frequency.png")


# ╔══════════════════════════════════════════════════════════════╗
# ║  Q3 – House Prices Histogram & Normality Check               ║
# ╚══════════════════════════════════════════════════════════════╝
banner("House Prices – Histogram & Normality Analysis", 3)

df3 = pd.read_csv(os.path.join(DATASETS, "house_prices.csv"))
price_col = "Price" if "Price" in df3.columns else df3.select_dtypes("number").columns[0]
prices = df3[price_col].dropna()

skewness = prices.skew()
kurtosis = prices.kurt()
stat, p_value = stats.shapiro(prices[:5000])  # Shapiro-Wilk (max 5000)
_, p_ks = stats.kstest(prices, "norm", args=(prices.mean(), prices.std()))

print(f"\n--- House Price Statistics ---")
print(f"  Mean      : {prices.mean():,.2f}")
print(f"  Median    : {prices.median():,.2f}")
print(f"  Std Dev   : {prices.std():,.2f}")
print(f"  Skewness  : {skewness:.4f}")
print(f"  Kurtosis  : {kurtosis:.4f}")
print(f"\n--- Normality Tests ---")
print(f"  Shapiro-Wilk  : stat={stat:.4f}, p={p_value:.6f}")
print(f"  KS Test       : p={p_ks:.6f}")
if abs(skewness) < 0.5:
    dist_desc = "Approximately Normally Distributed (|skew| < 0.5)"
elif skewness > 0.5:
    dist_desc = "Right (Positively) Skewed"
else:
    dist_desc = "Left (Negatively) Skewed"
print(f"\n  Distribution: {dist_desc}")

fig, axes = plt.subplots(1, 3, figsize=(18, 6))
fig.suptitle("Q3 – House Prices Distribution Analysis", fontsize=18)

# Histogram with KDE
ax = axes[0]
ax.hist(prices, bins=40, density=True, color=ACCENT, alpha=0.7, edgecolor="#21262d", label="Histogram")
kde_x = np.linspace(prices.min(), prices.max(), 300)
kde = stats.gaussian_kde(prices)
ax.plot(kde_x, kde(kde_x), color=SUCCESS, linewidth=2.5, label="KDE")
ax.axvline(prices.mean(), color=WARNING, linestyle="--", linewidth=2, label=f"Mean: {prices.mean():.1f}")
ax.axvline(prices.median(), color=DANGER, linestyle="--", linewidth=2, label=f"Median: {prices.median():.1f}")
ax.set_title("Price Histogram + KDE")
ax.set_xlabel(price_col)
ax.set_ylabel("Density")
ax.legend(fontsize=9)
ax.text(0.97, 0.95, f"Skew: {skewness:.3f}\nKurt: {kurtosis:.3f}",
        transform=ax.transAxes, ha="right", va="top",
        bbox=dict(boxstyle="round", fc="#21262d", alpha=0.8),
        fontsize=10, color="#e6edf3")

# Q-Q Plot
ax = axes[1]
qq = stats.probplot(prices, dist="norm")
ax.plot(qq[0][0], qq[0][1], "o", color=ACCENT, markersize=4, alpha=0.6, label="Data")
slope, intercept = np.polyfit(qq[0][0], qq[0][1], 1)
ax.plot(qq[0][0], slope * qq[0][0] + intercept, "-", color=DANGER, linewidth=2, label="Normal Line")
ax.set_title("Q-Q Plot (Normality Check)")
ax.set_xlabel("Theoretical Quantiles")
ax.set_ylabel("Sample Quantiles")
ax.legend()

# Box plot
ax = axes[2]
bp = ax.boxplot(prices, patch_artist=True, widths=0.5,
                boxprops=dict(facecolor=ACCENT, alpha=0.7),
                medianprops=dict(color=SUCCESS, linewidth=2),
                whiskerprops=dict(color="#8b949e"),
                capprops=dict(color="#8b949e"),
                flierprops=dict(marker="o", color=DANGER, alpha=0.5))
ax.set_title("Price Box Plot")
ax.set_ylabel(price_col)
ax.set_xticklabels(["Price"])

plt.tight_layout()
save_fig("Q3_house_prices.png")


# ╔══════════════════════════════════════════════════════════════╗
# ║  Q4 – Salary Box Plot & Outlier Identification               ║
# ╚══════════════════════════════════════════════════════════════╝
banner("Salary Data – Box Plot & Outlier Identification", 4)

df4 = pd.read_csv(os.path.join(DATASETS, "salary_data.csv"))
sal = df4["Salary"].dropna()

Q1_s, Q3_s = sal.quantile(0.25), sal.quantile(0.75)
IQR_s = Q3_s - Q1_s
lower_s = Q1_s - 1.5 * IQR_s
upper_s = Q3_s + 1.5 * IQR_s
outliers_s = sal[(sal < lower_s) | (sal > upper_s)]

print(f"\n--- Salary Statistics ---")
print(f"  Mean   : {sal.mean():,.2f}")
print(f"  Median : {sal.median():,.2f}")
print(f"  Q1     : {Q1_s:,.2f}")
print(f"  Q3     : {Q3_s:,.2f}")
print(f"  IQR    : {IQR_s:,.2f}")
print(f"  Lower Fence : {lower_s:,.2f}")
print(f"  Upper Fence : {upper_s:,.2f}")
print(f"\n--- Outliers Detected ---")
print(f"  Count  : {len(outliers_s)}")
print(f"  Values : {sorted(outliers_s.values)}")

fig, axes = plt.subplots(1, 3, figsize=(18, 7))
fig.suptitle("Q4 – Salary Box Plot & Outlier Analysis", fontsize=18)

# Box plot by role
ax = axes[0]
roles_order = ["Junior", "Mid", "Senior", "Lead", "Manager", "Director", "VP", "C-Level"]
role_salaries = [df4[df4["Role"] == r]["Salary"].dropna().values for r in roles_order if r in df4["Role"].unique()]
roles_present = [r for r in roles_order if r in df4["Role"].unique()]
bp = ax.boxplot(role_salaries, patch_artist=True,
                labels=roles_present,
                boxprops=dict(facecolor=ACCENT, alpha=0.6),
                medianprops=dict(color=SUCCESS, linewidth=2.5),
                flierprops=dict(marker="D", color=DANGER, markersize=5, alpha=0.7))
ax.set_title("Salary by Role (Box Plot)")
ax.set_xlabel("Role")
ax.set_ylabel("Salary ($)")
ax.set_xticklabels(roles_present, rotation=45, ha="right")

# Overall box plot
ax = axes[1]
bp2 = ax.boxplot(sal, patch_artist=True, widths=0.5,
                 boxprops=dict(facecolor=ACCENT, alpha=0.7),
                 medianprops=dict(color=SUCCESS, linewidth=2.5),
                 flierprops=dict(marker="D", color=DANGER, markersize=7, alpha=0.8, label="Outliers"))
ax.axhline(lower_s, color=WARNING, linestyle="--", linewidth=1.5, label=f"Lower Fence: {lower_s:,.0f}")
ax.axhline(upper_s, color=DANGER, linestyle="--", linewidth=1.5, label=f"Upper Fence: {upper_s:,.0f}")
ax.set_title("Overall Salary Box Plot")
ax.set_ylabel("Salary ($)")
ax.set_xticklabels(["All Employees"])
ax.legend(fontsize=9)

# Violin plot
ax = axes[2]
parts = ax.violinplot(sal, showmeans=True, showmedians=True)
for pc in parts["bodies"]:
    pc.set_facecolor(PALETTE[3])
    pc.set_alpha(0.7)
parts["cmeans"].set_color(WARNING)
parts["cmedians"].set_color(SUCCESS)
ax.scatter(np.ones(len(outliers_s)), outliers_s, color=DANGER, zorder=5,
           s=50, label="Outliers", alpha=0.8)
ax.set_title("Salary Violin Plot")
ax.set_ylabel("Salary ($)")
ax.set_xticks([1])
ax.set_xticklabels(["Salary"])
ax.legend()

plt.tight_layout()
save_fig("Q4_salary_boxplot.png")


# ╔══════════════════════════════════════════════════════════════╗
# ║  Q5 – Student Marks IQR Outlier Detection                    ║
# ╚══════════════════════════════════════════════════════════════╝
banner("Student Marks – IQR Outlier Detection", 5)

df5 = pd.read_csv(os.path.join(DATASETS, "student_marks.csv"))
mark_cols = ["Math", "Science", "English"]

outlier_report = {}
print("\n--- IQR Outlier Detection Results ---")
for col in mark_cols:
    data = df5[col].dropna()
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    out_idx = df5[(df5[col] < lower) | (df5[col] > upper)].index
    out_vals = df5.loc[out_idx, col].values
    outlier_report[col] = {"Q1": Q1, "Q3": Q3, "IQR": IQR,
                            "Lower": lower, "Upper": upper,
                            "Outlier Indices": list(out_idx),
                            "Outlier Values": list(out_vals)}
    print(f"\n  {col}:")
    print(f"    Q1={Q1:.2f}, Q3={Q3:.2f}, IQR={IQR:.2f}")
    print(f"    Fence: [{lower:.2f}, {upper:.2f}]")
    print(f"    Outliers ({len(out_vals)}): {sorted(out_vals)}")

fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle("Q5 – Student Marks: IQR Outlier Detection", fontsize=18)

for i, col in enumerate(mark_cols):
    data = df5[col].dropna()
    info = outlier_report[col]
    out_mask = (data < info["Lower"]) | (data > info["Upper"])

    # Histogram
    ax = axes[0, i]
    ax.hist(data[~out_mask], bins=20, color=ACCENT, alpha=0.7, label="Normal", edgecolor="#21262d")
    ax.hist(data[out_mask],  bins=20, color=DANGER,  alpha=0.9, label="Outliers", edgecolor="#21262d")
    ax.axvline(info["Lower"], color=WARNING, linestyle="--", linewidth=2, label=f"L: {info['Lower']:.1f}")
    ax.axvline(info["Upper"], color=WARNING, linestyle="--", linewidth=2, label=f"U: {info['Upper']:.1f}")
    ax.set_title(f"{col} – Histogram")
    ax.set_xlabel("Marks")
    ax.set_ylabel("Frequency")
    ax.legend(fontsize=8)

    # Box plot
    ax = axes[1, i]
    bp = ax.boxplot(data, patch_artist=True, widths=0.5,
                    boxprops=dict(facecolor=ACCENT, alpha=0.7),
                    medianprops=dict(color=SUCCESS, linewidth=2.5),
                    flierprops=dict(marker="D", color=DANGER, markersize=8))
    ax.set_title(f"{col} – Box Plot")
    ax.set_ylabel("Marks")
    ax.set_xticklabels([col])
    ax.text(1.25, info["Lower"], f"Lower: {info['Lower']:.1f}", color=WARNING, fontsize=9, va="center")
    ax.text(1.25, info["Upper"], f"Upper: {info['Upper']:.1f}", color=WARNING, fontsize=9, va="center")

plt.tight_layout()
save_fig("Q5_student_marks_IQR.png")


# ╔══════════════════════════════════════════════════════════════╗
# ║  Q6 – Sales Dataset IQR Outlier Removal                      ║
# ╚══════════════════════════════════════════════════════════════╝
banner("Sales Dataset – IQR Outlier Removal", 6)

df6 = pd.read_csv(os.path.join(DATASETS, "sales_data.csv"))
col6 = "SalesAmount"
data6 = df6[col6].dropna()

Q1_6 = data6.quantile(0.25)
Q3_6 = data6.quantile(0.75)
IQR_6 = Q3_6 - Q1_6
lower_6 = Q1_6 - 1.5 * IQR_6
upper_6 = Q3_6 + 1.5 * IQR_6

df6_clean = df6[(df6[col6] >= lower_6) & (df6[col6] <= upper_6)].copy()

print(f"\n--- IQR Parameters ---")
print(f"  Q1 = {Q1_6:,.2f}")
print(f"  Q3 = {Q3_6:,.2f}")
print(f"  IQR = {IQR_6:,.2f}")
print(f"  Lower Fence = {lower_6:,.2f}")
print(f"  Upper Fence = {upper_6:,.2f}")
print(f"\n--- Before Cleaning ---")
print(f"  Rows    : {len(df6)}")
print(f"  Mean    : {data6.mean():,.2f}")
print(f"  Std Dev : {data6.std():,.2f}")
print(f"\n--- After Cleaning ---")
print(f"  Rows    : {len(df6_clean)}")
print(f"  Removed : {len(df6) - len(df6_clean)} outliers")
print(f"  Mean    : {df6_clean[col6].mean():,.2f}")
print(f"  Std Dev : {df6_clean[col6].std():,.2f}")

# Save cleaned dataset
cleaned_path = os.path.join(OUTPUTS, "sales_data_cleaned.csv")
df6_clean.to_csv(cleaned_path, index=False)
print(f"\n  [Saved] outputs/sales_data_cleaned.csv ({len(df6_clean)} rows)")

print("\n--- First 10 Rows of Cleaned Dataset ---")
print(df6_clean.head(10).to_string(index=False))

fig, axes = plt.subplots(1, 3, figsize=(18, 6))
fig.suptitle("Q6 – Sales Data: IQR Outlier Removal", fontsize=18)

# Before
ax = axes[0]
ax.hist(df6[col6], bins=30, color=DANGER, alpha=0.8, edgecolor="#21262d")
ax.axvline(lower_6, color=WARNING, linestyle="--", linewidth=2, label=f"L: {lower_6:,.0f}")
ax.axvline(upper_6, color=WARNING, linestyle="--", linewidth=2, label=f"U: {upper_6:,.0f}")
ax.set_title(f"Before – {len(df6)} rows")
ax.set_xlabel("Sales Amount ($)")
ax.set_ylabel("Frequency")
ax.legend(fontsize=9)

# After
ax = axes[1]
ax.hist(df6_clean[col6], bins=30, color=SUCCESS, alpha=0.8, edgecolor="#21262d")
ax.set_title(f"After – {len(df6_clean)} rows")
ax.set_xlabel("Sales Amount ($)")
ax.set_ylabel("Frequency")

# Side-by-side box plot
ax = axes[2]
ax.boxplot([df6[col6].dropna(), df6_clean[col6].dropna()],
           labels=["Before", "After"],
           patch_artist=True,
           boxprops=dict(facecolor=ACCENT, alpha=0.7),
           medianprops=dict(color=SUCCESS, linewidth=2.5),
           flierprops=dict(marker="D", color=DANGER, markersize=6))
ax.set_title("Box Plot: Before vs After")
ax.set_ylabel("Sales Amount ($)")

plt.tight_layout()
save_fig("Q6_sales_outlier_removal.png")


# ╔══════════════════════════════════════════════════════════════╗
# ║  Q7 – Before/After Outlier Visualisation (Histogram+BoxPlot) ║
# ╚══════════════════════════════════════════════════════════════╝
banner("Pollution Data – Histograms & Box Plots Before/After Outlier Removal", 7)

df7 = pd.read_csv(os.path.join(DATASETS, "pollution_data.csv"))
cols7 = ["PM2_5", "NO2", "CO"]

cleaned_datasets = {}
for col in cols7:
    s = df7[col].dropna()
    Q1 = s.quantile(0.25)
    Q3 = s.quantile(0.75)
    IQR = Q3 - Q1
    cleaned = s[(s >= Q1 - 1.5 * IQR) & (s <= Q3 + 1.5 * IQR)]
    cleaned_datasets[col] = cleaned
    removed = len(s) - len(cleaned)
    print(f"  {col}: {removed} outliers removed ({len(cleaned)} remain)")

fig = plt.figure(figsize=(20, 12))
fig.suptitle("Q7 – Before & After Outlier Removal: Histograms & Box Plots", fontsize=18, y=1.01)

for idx, col in enumerate(cols7):
    raw = df7[col].dropna()
    clean = cleaned_datasets[col]

    # Histogram Before
    ax1 = fig.add_subplot(4, 3, idx + 1)
    ax1.hist(raw, bins=30, color=DANGER, alpha=0.75, edgecolor="#21262d")
    ax1.set_title(f"{col} – Hist (Before)", fontsize=11)
    ax1.set_ylabel("Freq")

    # Histogram After
    ax2 = fig.add_subplot(4, 3, idx + 4)
    ax2.hist(clean, bins=30, color=SUCCESS, alpha=0.75, edgecolor="#21262d")
    ax2.set_title(f"{col} – Hist (After)", fontsize=11)
    ax2.set_ylabel("Freq")

    # Box Plot Before
    ax3 = fig.add_subplot(4, 3, idx + 7)
    ax3.boxplot(raw, patch_artist=True,
                boxprops=dict(facecolor=DANGER, alpha=0.6),
                medianprops=dict(color="#e6edf3", linewidth=2),
                flierprops=dict(marker="o", color=DANGER, alpha=0.5))
    ax3.set_title(f"{col} – Box (Before)", fontsize=11)
    ax3.set_xticklabels([col])

    # Box Plot After
    ax4 = fig.add_subplot(4, 3, idx + 10)
    ax4.boxplot(clean, patch_artist=True,
                boxprops=dict(facecolor=SUCCESS, alpha=0.6),
                medianprops=dict(color="#e6edf3", linewidth=2),
                flierprops=dict(marker="o", color=SUCCESS, alpha=0.5))
    ax4.set_title(f"{col} – Box (After)", fontsize=11)
    ax4.set_xticklabels([col])

plt.tight_layout()
save_fig("Q7_before_after_outliers.png")


# ╔══════════════════════════════════════════════════════════════╗
# ║  Q8 – Titanic EDA                                            ║
# ╚══════════════════════════════════════════════════════════════╝
banner("Titanic Dataset – Full Exploratory Data Analysis", 8)

df8 = pd.read_csv(os.path.join(DATASETS, "titanic.csv"))

# 1. Dataset Info
print("\n--- 1. Dataset Information ---")
print(f"  Shape: {df8.shape[0]} rows × {df8.shape[1]} columns")
print(f"  Columns: {list(df8.columns)}")
print(df8.dtypes.to_string())

# 2. Missing Values
print("\n--- 2. Missing Values ---")
mv = df8.isnull().sum()
mv_pct = (mv / len(df8) * 100).round(2)
mv_df = pd.DataFrame({"Missing": mv, "Pct %": mv_pct})
print(mv_df[mv_df["Missing"] > 0].to_string())

# 3. Descriptive Statistics
print("\n--- 3. Descriptive Statistics ---")
print(df8.describe().round(2).to_string())

# 4. Outlier Detection (Age, Fare)
num_cols_8 = ["Age", "Fare"]
outlier_8 = {}
print("\n--- 6. Outlier Detection (IQR Method) ---")
for col in num_cols_8:
    if col in df8.columns:
        s = df8[col].dropna()
        Q1 = s.quantile(0.25)
        Q3 = s.quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        outs = s[(s < lower) | (s > upper)]
        outlier_8[col] = (lower, upper, outs)
        print(f"  {col}: fence=[{lower:.2f}, {upper:.2f}], outliers={len(outs)}")

# 5. Remove Outliers
df8_clean = df8.copy()
for col in num_cols_8:
    if col in df8.columns:
        lower, upper, _ = outlier_8[col]
        df8_clean = df8_clean[(df8_clean[col].isna()) |
                              ((df8_clean[col] >= lower) & (df8_clean[col] <= upper))]

print(f"\n--- 7. Outlier Removal ---")
print(f"  Before: {len(df8)} rows")
print(f"  After : {len(df8_clean)} rows")
print(f"  Removed: {len(df8) - len(df8_clean)} rows")

# 6. Save Cleaned Dataset
cleaned_titanic_path = os.path.join(OUTPUTS, "titanic_cleaned.csv")
df8_clean.to_csv(cleaned_titanic_path, index=False)
print(f"\n  [Saved] outputs/titanic_cleaned.csv ({len(df8_clean)} rows)")

# 7. Visualisations
fig = plt.figure(figsize=(20, 20))
fig.suptitle("Q8 – Titanic EDA Dashboard", fontsize=20, y=1.01)

# Missing values
ax1 = fig.add_subplot(4, 3, 1)
mv_plot = mv[mv > 0]
bars = ax1.bar(mv_plot.index, mv_plot.values, color=DANGER, alpha=0.85, edgecolor="#21262d")
ax1.set_title("Missing Values")
ax1.set_ylabel("Count")
ax1.set_xticklabels(mv_plot.index, rotation=45, ha="right")
for bar in bars:
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
             str(int(bar.get_height())), ha="center", va="bottom", fontsize=9)

# Survival count
ax2 = fig.add_subplot(4, 3, 2)
surv = df8["Survived"].value_counts()
ax2.bar(["Did Not Survive", "Survived"], surv.values,
        color=[DANGER, SUCCESS], edgecolor="#21262d", alpha=0.85)
ax2.set_title("Survival Count")
ax2.set_ylabel("Count")

# Pclass distribution
ax3 = fig.add_subplot(4, 3, 3)
pclass = df8["Pclass"].value_counts().sort_index()
ax3.bar([f"Class {c}" for c in pclass.index], pclass.values,
        color=PALETTE[:3], edgecolor="#21262d", alpha=0.85)
ax3.set_title("Passenger Class Distribution")
ax3.set_ylabel("Count")

# Age histogram (before)
ax4 = fig.add_subplot(4, 3, 4)
ax4.hist(df8["Age"].dropna(), bins=25, color=ACCENT, alpha=0.8, edgecolor="#21262d")
ax4.set_title("Age Distribution (Before)")
ax4.set_xlabel("Age")
ax4.set_ylabel("Frequency")

# Age histogram (after)
ax5 = fig.add_subplot(4, 3, 5)
ax5.hist(df8_clean["Age"].dropna(), bins=25, color=SUCCESS, alpha=0.8, edgecolor="#21262d")
ax5.set_title("Age Distribution (After Outlier Removal)")
ax5.set_xlabel("Age")
ax5.set_ylabel("Frequency")

# Fare histogram (before)
ax6 = fig.add_subplot(4, 3, 6)
ax6.hist(df8["Fare"].dropna(), bins=40, color=PALETTE[3], alpha=0.8, edgecolor="#21262d")
ax6.set_title("Fare Distribution (Before)")
ax6.set_xlabel("Fare ($)")
ax6.set_ylabel("Frequency")

# Fare histogram (after)
ax7 = fig.add_subplot(4, 3, 7)
ax7.hist(df8_clean["Fare"].dropna(), bins=40, color=SUCCESS, alpha=0.8, edgecolor="#21262d")
ax7.set_title("Fare Distribution (After Outlier Removal)")
ax7.set_xlabel("Fare ($)")
ax7.set_ylabel("Frequency")

# Age box plot (before/after)
ax8 = fig.add_subplot(4, 3, 8)
age_data = [df8["Age"].dropna(), df8_clean["Age"].dropna()]
ax8.boxplot(age_data, labels=["Before", "After"], patch_artist=True,
            boxprops=dict(facecolor=ACCENT, alpha=0.7),
            medianprops=dict(color=SUCCESS, linewidth=2.5),
            flierprops=dict(marker="D", color=DANGER, markersize=6))
ax8.set_title("Age Box Plot: Before vs After")
ax8.set_ylabel("Age")

# Fare box plot (before/after)
ax9 = fig.add_subplot(4, 3, 9)
fare_data = [df8["Fare"].dropna(), df8_clean["Fare"].dropna()]
ax9.boxplot(fare_data, labels=["Before", "After"], patch_artist=True,
            boxprops=dict(facecolor=PALETTE[3], alpha=0.7),
            medianprops=dict(color=SUCCESS, linewidth=2.5),
            flierprops=dict(marker="D", color=DANGER, markersize=6))
ax9.set_title("Fare Box Plot: Before vs After")
ax9.set_ylabel("Fare ($)")

# Gender distribution
ax10 = fig.add_subplot(4, 3, 10)
gender = df8["Sex"].value_counts()
wedges, texts, autotexts = ax10.pie(gender.values, labels=gender.index,
                                     autopct="%1.1f%%", colors=[ACCENT, PALETTE[3]],
                                     startangle=90, textprops={"color": "#e6edf3", "fontsize": 10})
ax10.set_facecolor("#0d1117")
ax10.set_title("Gender Distribution")

# Survival by class
ax11 = fig.add_subplot(4, 3, 11)
surv_class = df8.groupby("Pclass")["Survived"].mean() * 100
ax11.bar([f"Class {c}" for c in surv_class.index], surv_class.values,
         color=PALETTE[:3], edgecolor="#21262d", alpha=0.85)
ax11.set_title("Survival Rate by Class (%)")
ax11.set_ylabel("Survival Rate (%)")

# Age by survival
ax12 = fig.add_subplot(4, 3, 12)
age_surv0 = df8[df8["Survived"] == 0]["Age"].dropna()
age_surv1 = df8[df8["Survived"] == 1]["Age"].dropna()
ax12.hist(age_surv0, bins=20, alpha=0.6, color=DANGER, label="Did Not Survive", edgecolor="#21262d")
ax12.hist(age_surv1, bins=20, alpha=0.6, color=SUCCESS, label="Survived", edgecolor="#21262d")
ax12.set_title("Age by Survival Status")
ax12.set_xlabel("Age")
ax12.set_ylabel("Frequency")
ax12.legend(fontsize=9)

plt.tight_layout()
save_fig("Q8_titanic_EDA.png")


# ╔══════════════════════════════════════════════════════════════╗
# ║  FINAL SUMMARY                                               ║
# ╚══════════════════════════════════════════════════════════════╝
print("\n" + "=" * 70)
print("  ALL QUESTIONS COMPLETED!")
print("=" * 70)
print(f"\n  Outputs saved to: {OUTPUTS}")
print("\n  Files generated:")
for f in sorted(os.listdir(OUTPUTS)):
    fpath = os.path.join(OUTPUTS, f)
    size = os.path.getsize(fpath)
    print(f"    * {f}  ({size:,} bytes)")
print()
print("="*70)
print("Execution Completed Successfully.")
print("="*70)

log.close()