# case 3
# Monthly spend of each customer
import pandas as pd

# Assuming the data is stored in an Excel file named "Credit_Banking_Project1.xlsx"
df = pd.read_excel("Credit_Banking_Project1.xlsx")

# Grouping the data by customer_id and calculating the sum of spend for each customer
monthly_spend = df.groupby('Customer')['Amount_spend'].sum()

# Print the monthly spend of each customer
for customer, spend in monthly_spend.items():
    print(f"Customer: {customer}, Monthly Spend: {spend}")

