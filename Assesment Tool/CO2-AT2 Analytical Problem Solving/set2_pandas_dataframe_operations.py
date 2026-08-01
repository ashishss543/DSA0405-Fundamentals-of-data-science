import pandas as pd

print("--- 1. Creating Sample DataFrame ---")
# Creating a DataFrame manually
df = pd.DataFrame()

df['Name'] = ['John', 'Emma', 'Liam', 'Olivia']
df['Age'] = [20, 19, 21, 18]
df['Student'] = [True, True, False, True]

print("Initial DataFrame:")
print(df)
print()

print("--- 2. Adding Row to DataFrame ---")
# Using pd.concat to append a new record
new_row = pd.DataFrame([['Sophia', 22, False]], columns=['Name', 'Age', 'Student'])
df = pd.concat([df, new_row], ignore_index=True)

print("DataFrame after adding row:")
print(df)
