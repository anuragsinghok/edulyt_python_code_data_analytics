# case 4
# Monthly repayment of each customer
import pandas as pd


df = pd.read_excel("Credit_Banking_Project.xls")

# Grouping the data by customer_id and calculating the sum of repayment for each customer
monthly_repayment = df.groupby('Customer')['Amount_repayment'].sum()

# Print the monthly repayment of each customer
for customer, repayment in monthly_repayment.items():
    print(f"Customer: {customer}, Monthly Repayment: {repayment}")

