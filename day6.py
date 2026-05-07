import pandas as pd
import io

# 1. SETUP DATASET
# Simulating the CSV data provided in the project description
data = """PRODUCT,QUANTITY,PRICE
A,2,100
B,1,200
A,3,100
C,5,500"""

# Reading the CSV data into a DataFrame
df = pd.read_csv(io.StringIO(data))

# 2. COLUMN OPERATIONS (Bonus Task)
# Calculate total for each row: Total = Quantity * Price
df['TOTAL'] = df['QUANTITY'] * df['PRICE']

# 3. BASIC AGGREGATION
# Calculate Total Sales (Revenue) per Product
product_sales = df.groupby('PRODUCT')['TOTAL'].sum().reset_index()

# 4. SORT BY REVENUE (Bonus Task)
product_sales = product_sales.sort_values(by='TOTAL', ascending=False)

# 5. FIND TOTAL REVENUE & TOP-SELLING PRODUCT
total_revenue = product_sales['TOTAL'].sum()
top_selling_product = product_sales.iloc[0]['PRODUCT']

# --- OUTPUT RESULTS ---

print("--- Full Dataset with New Column ---")
print(df)
print("\n--- Sales per Product (Sorted) ---")
print(product_sales)
print("\n--- Summary Statistics ---")
print(f"Total Revenue: {total_revenue}")
print(f"Top-Selling Product: {top_selling_product}")