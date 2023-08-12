import pandas as pd

interest_rate = 0.029  # 2.9% interest rate (given)

data_spend = pd.read_excel("Credit Banking Projecti part 2.xlsx")
monthly_spend = data_spend.groupby('Customer')['Amount spend'].sum()

data_repayment = pd.read_excel("Credit Banking_ Projecti part 2.xlsx")
monthly_repayment = data_repayment.groupby('Customer')['Amount repayment '].sum()

due_amount = monthly_spend - monthly_repayment
interest_amount = due_amount * interest_rate
updated_due_amount = due_amount + interest_amount

# Create a new DataFrame with the updated due amount including interest
data_updated = pd.DataFrame({'Customer': due_amount.index, 'Due Amount': updated_due_amount})

# Print the updated DataFrame with the due amount including interest
print(data_updated)

