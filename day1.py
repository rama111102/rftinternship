# Python Internship Day 1
# Project 1 - Data Cleaner

# Original list
data = [10, None, 20, 10, "", 30, None, 40]

# Empty list to store clean data
clean_list = []

# Counter for removed values
removed = 0

# Loop through each item
for item in data:
    
    # Check invalid values
    if item is None or item == "":
        removed += 1
    
    # Check duplicate values
    elif item not in clean_list:
        clean_list.append(item)
    
    else:
        removed += 1

# Sort final clean list
clean_list.sort()

# Show result
print("Original List:", data)
print("Clean List:", clean_list)
print("Total Removed:", removed)