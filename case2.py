 # case 2
# Identity where the repayment is more than the spend
# then give them a credit of 28 of their surplus
# amount in the next month billing.
# from
# Monthly spend of each customer
import pandas as pd

# Assuming the spend data is stored in an Excel file named "Credit_Banking_Project1.xlsx"
spend_data = pd.read_excel("Credit_Banking_Project1.xlsx")

# Grouping the spend data by customer_id and calculating the sum of spend for each customer
monthly_spend = spend_data.groupby('Customer')['Amount_spend'].sum()

# Assuming the repayment data is stored in an Excel file named "Credit_Banking_Project2.xlsx"
repayment_data = pd.read_excel("Credit_Banking_Project2.xlsx")

# Grouping the repayment data by customer_id and calculating the sum of repayment for each customer
monthly_repayment = repayment_data.groupby('Customer')['Amount_repayment'].sum()

# Calculate surplus and assign credit for positive surplus
repayment_data['surplus'] = repayment_data['Amount_repayment'] - repayment_data['Amount_spend']
repayment_data['credit'] = repayment_data.loc[repayment_data['surplus'] > 0, 'surplus'] * 0.02

# Print the credit for customers with positive surplus
print(repayment_data.loc[repayment_data['surplus'] > 0, 'credit'])
