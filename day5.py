# 1. READ FILE
file_name = 'data.csv'

# Creating the file for demonstration purposes
with open(file_name, 'w') as f:
    f.write("NAME,AGE,MARKS\n")
    f.write("AMIT,20,85\n")
    f.write("RIYA,21,90")

# --- ACTUAL PROGRAM STARTS HERE ---

data_list = []

with open(file_name, 'r') as file:
    # Get the headers from the first line
    headers = file.readline().strip().split(',')
    
    # Process each data row
    for line in file:
        # STRING SPLITTING
        values = line.strip().split(',')
        
        # DATA STRUCTURING (Create dictionary for each row)
        row_dict = {
            headers[0]: values[0],           # NAME
            headers[1]: int(values[1]),      # AGE (Converted to int)
            headers[2]: int(values[2])       # MARKS (Converted to int)
        }
        
        # Store in list
        data_list.append(row_dict)

# OUTPUT
print(data_list)