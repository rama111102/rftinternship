import pandas as pd

# 1. Create the dataset
data = {
    'NAME': ['A', 'B', 'C', 'D'],
    'DEPT': ['IT', 'HR', 'IT', 'HR'],
    'SALARY': [50000, 40000, 60000, 45000]
}

df = pd.DataFrame(data)

print("--- Original Dataset ---")
print(df)
print("\n")

# 2. Find Average Salary per Department
# We group by 'DEPT' and then take the mean (average) of the 'SALARY' column
avg_salary = df.groupby('DEPT')['SALARY'].mean()

# 3. Find Highest Paid Employee per Department
# We group by 'DEPT' and take the max value of the 'SALARY' column
max_salary = df.groupby('DEPT')['SALARY'].max()

# --- BONUS TASKS ---

# 4. Count Employees per Department
# We group by 'DEPT' and count the number of entries in 'NAME'
emp_count = df.groupby('DEPT')['NAME'].count()

# 5. Sort Departments by Average Salary
# We take our avg_salary result and sort it (ascending=False makes it highest to lowest)
sorted_avg = avg_salary.sort_values(ascending=False)

# --- DISPLAYING RESULTS ---

print("--- Results ---")
print("Average Salary per Dept:\n", avg_salary)
print("\nHighest Salary per Dept:\n", max_salary)
print("\nEmployee Count per Dept:\n", emp_count)
print("\nDepartments sorted by Avg Salary:\n", sorted_avg)