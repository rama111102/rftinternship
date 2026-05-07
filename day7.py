import pandas as pd

# 1. SETUP DATASET
data = {
    'NAME': ['AMIT', 'RIYA', 'JOHN'],
    'MATH': [80, 90, 60],
    'SCIENCE': [70, 88, 65],
    'ENGLISH': [85, 92, 70]
}

df = pd.DataFrame(data)

# --- TASK 1: CALCULATE AVERAGE MARKS PER STUDENT ---
# Column Thinking: Creating a new column based on row-wise math
subjects = ['MATH', 'SCIENCE', 'ENGLISH']
df['AVERAGE'] = df[subjects].mean(axis=1)

# --- TASK 2: FIND TOPPER ---
# Aggregation: Finding the row with the maximum average
topper = df.loc[df['AVERAGE'].idxmax()]

# --- TASK 3: COUNT STUDENTS ABOVE AVERAGE ---
# Filtering: Comparing student averages to the overall class average
class_avg = df['AVERAGE'].mean()
students_above_avg = df[df['AVERAGE'] > class_avg]
count_above_avg = len(students_above_avg)

# --- BONUS 1: ADD GRADE COLUMN ---
# Logic-based column creation
def calculate_grade(avg):
    if avg >= 85: return 'A'
    elif avg >= 75: return 'B'
    else: return 'C'

df['GRADE'] = df['AVERAGE'].apply(calculate_grade)

# --- BONUS 2: SUBJECT-WISE AVERAGE ---
# Column Thinking: Aggregating vertically down each column
subject_averages = df[subjects].mean()

# --- DISPLAY DASHBOARD ---
print("--- STUDENT PERFORMANCE DASHBOARD ---")
print(df)
print("-" * 40)
print(f"Topper of the class: {topper['NAME']} with {topper['AVERAGE']:.2f}%")
print(f"Number of students above class average ({class_avg:.2f}%): {count_above_avg}")
print("-" * 40)
print("Subject-wise Averages:")
print(subject_averages)