def calculate_stats(marks):
    avg = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)
    return avg, highest, lowest

def count_above_average(marks, average):
    count = 0
    for m in marks:
        if m > average:
            count += 1
    return count

def get_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    else:
        return 'FAIL'

# Main
marks = [78, 85, 90, 67, 85, 92, 78]

average, highest, lowest = calculate_stats(marks)
above_avg_count = count_above_average(marks, average)
grade = get_grade(average)

print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
print("Above Average Count:", above_avg_count)
print("Grade:", grade)