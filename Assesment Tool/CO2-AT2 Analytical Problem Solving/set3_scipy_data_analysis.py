import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import norm, pearsonr
from scipy import linalg
from scipy.optimize import minimize

print("==================================================")
print("             DATA ANALYSIS WITH SCIPY            ")
print("==================================================")

# 1. Measures of Central Tendency Using SciPy
print("\n1. Measures of Central Tendency Using SciPy:")
data = [10, 20, 30, 40, 50]
print("Dataset:", data)
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Mode:", stats.mode(data))

# 2. Probability Distribution Analysis Using SciPy
print("\n2. Probability Distribution Analysis Using SciPy:")
# loc=70 specifies mean, scale=10 specifies std dev
probability = norm.cdf(85, loc=70, scale=10)
print("Cumulative Probability P(X <= 85) for Mean=70, StdDev=10:", probability)

# 3. Hypothesis Testing
print("\n3. Hypothesis Testing:")
data_sample = [22, 25, 19, 24, 28, 30]
t_stat, p_value = stats.ttest_1samp(data_sample, 25)
print("Sample Data:", data_sample)
print("T-Statistic:", t_stat)
print("P-Value:", p_value)

# 4. Correlation Analysis
print("\n4. Correlation Analysis:")
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
corr, p_val_corr = pearsonr(x, y)
print("X:", x)
print("Y:", y)
print("Pearson Correlation Coefficient:", corr)
print("P-Value:", p_val_corr)

# 5. Linear Algebra Operations
print("\n5. Linear Algebra Operations:")
A = [[3, 2], [1, 2]]
B = [5, 5]
solution = linalg.solve(A, B)
print("Matrix A:", A)
print("Vector B:", B)
print("Solution [x, y]:", solution)

# 6. Optimization Using SciPy
print("\n6. Optimization Using SciPy:")
def objective(x):
    return x**2 + 4

result = minimize(objective, x0=5)
print("Objective function: f(x) = x^2 + 4")
print("Initial guess x0 = 5")
print("Optimal value of x:", result.x)
print("Minimum function value:", result.fun)
