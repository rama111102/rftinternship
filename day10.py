# Project 10 — Simple Log Analyzer
# Data provided in 37291.jpg
LOGS = [
    "ERROR DISK FULL",
    "INFO STARTED",
    "ERROR FILE MISSING",
    "WARNING MEMORY LOW"
]

def analyze_logs(log_list):
    # Initialize counters
    counts = {
        "ERROR": 0,
        "INFO": 0,
        "WARNING": 0
    }

    for log in log_list:
        # Bonus: Ignore case sensitivity by converting to uppercase
        upper_log = log.upper()
        
        # Pattern Detection/Counting
        if "ERROR" in upper_log:
            counts["ERROR"] += 1
        elif "INFO" in upper_log:
            counts["INFO"] += 1
        elif "WARNING" in upper_log:
            counts["WARNING"] += 1

    # Display basic counts
    print("--- Log Analysis Results ---")
    for log_type, total in counts.items():
        print(f"{log_type}: {total}")

    # Bonus: Find most frequent log type
    # Using max() with the dictionary values to find the top category
    most_frequent = max(counts, key=counts.get)
    
    print("\n--- Bonus Analysis ---")
    print(f"Most Frequent Log Type: {most_frequent}")

# Run the analyzer
analyze_logs(LOGS)