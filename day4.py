# The given logs list
logs = [
    "ERROR DISK FULL",
    "INFO STARTED",
    "ERROR FILE MISSING",
    "WARNING MEMORY LOW",
    "error connection lost" # Added one to test case sensitivity
]

# Initialize counts in a dictionary for easy pattern detection
counts = {"ERROR": 0, "INFO": 0, "WARNING": 0}

# Process the logs
for log in logs:
    # Bonus: Ignore case sensitivity by converting the string to uppercase
    upper_log = log.upper()
    
    # Check for keywords at the start of each string
    if upper_log.startswith("ERROR"):
        counts["ERROR"] += 1
    elif upper_log.startswith("INFO"):
        counts["INFO"] += 1
    elif upper_log.startswith("WARNING"):
        counts["WARNING"] += 1

# Display the results
print("--- Log Analysis Results ---")
for log_type, value in counts.items():
    print(f"{log_type}: {value}")

# Bonus: Find the most frequent log type
# This finds the key with the highest value in our dictionary
most_frequent = max(counts, key=counts.get)

print("----------------------------")
print(f"Most Frequent Log Type: {most_frequent} ({counts[most_frequent]} times)")