# case 5
# Highest paying 10 customers
# from monthly repayment of each customer
import pandas as pd

# Assuming the data is stored in an Excel file named "Credit_Banking_Project.xlsx"
df = pd.read_excel("Credit_Banking_Project.xlsx")

# Grouping the data by customer_id and calculating the sum of repayment for each customer
monthly_repayment = df.groupby('Customer')['Amount_repayment'].sum()

# Get the top 10 customers with the highest monthly repayment
top_10_customers = monthly_repayment.sort_values(ascending=False).head(10)

# Print the top 10 customers with the highest monthly repayment
print(top_10_customers)

