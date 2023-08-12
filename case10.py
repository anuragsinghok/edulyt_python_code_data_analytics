# case 10
# Monthly profit for the bank
# from
# Monthly spend of each customer
import pandas as pd

data_spend = pd.read_excel("Credit Banking Project1.xls")
data_repayment = pd.read_excel("Credit Banking Project1.xlsx")

# Grouping the spend data by customer ID and calculating the total spend for each customer
customer_monthly_spend = data_spend.groupby('Customer')['Amount spend'].sum()

# Grouping the repayment data by customer ID and calculating the total repayment for each customer
customer_monthly_repayment = data_repayment.groupby('Customer')['Amount repayment'].sum()

# Calculating the monthly profit for each customer
customer_monthly_profit = customer_monthly_spend - customer_monthly_repayment

print(customer_monthly_profit)
