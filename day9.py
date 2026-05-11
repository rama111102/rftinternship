import pandas as pd

# 1. GIVEN DATASET (Creating a sample set for the project)
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'Age': [25, 35, 28, 40, 22, 29],
    'Salary': [60000, 45000, 70000, 80000, 55000, 48000],
    'City': ['New York', 'London', 'Paris', 'Berlin', 'Dubai', 'Tokyo']
}

df = pd.DataFrame(data)

# 2. FOCUS: REPLACING IF-ELSE WITH FILTERS
# Instead of looping through each row with an 'if', we use Boolean Indexing.
# This creates a 'mask' of True/False values.

# Condition 1: Salary > 50000
# Condition 2: Age < 30
# BONUS: COMBINE MULTIPLE CONDITIONS using the '&' (AND) operator
filtered_df = df[(df['Salary'] > 50000) & (df['Age'] < 30)]

# 3. DISPLAY FILTERED RESULTS
print("--- Full Dataset ---")
print(df)
print("\n--- Filtered Results (Salary > 50k AND Age < 30) ---")
print(filtered_df)

# 4. BONUS: SAVE FILTERED DATA TO NEW FILE
# We will save this to a CSV file named 'filtered_employees.csv'
try:
    filtered_df.to_csv('filtered_employees.csv', index=False)
    print("\nSuccess: Filtered data has been saved to 'filtered_employees.csv'")
except Exception as e:
    print(f"\nError saving file: {e}")