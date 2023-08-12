# case 7
# indentifying which age group is spending more money from the
# Monthly spend of each customer
import numpy as np
import pandas as pd

data = pd.read_excel("Credit Banking Projecti part 2.xls")

# Grouping the data by customer ID and calculating the sum of spend for each customer
customer_spend = data.groupby('Customer')['Amount spend'].sum()

# Grouping the data by age group and calculating the sum of spend for each age group
age_bins = [0, 18, 30, 40, 50, np.inf]
age_labels = ['<18', '18-30', '31-40', '41-50', '50+']
data['Age group'] = pd.cut(data['Age'], bins=age_bins, labels=age_labels)
age_group_spend = data.groupby('Age group')['Amount spend'].sum()

# Finding the age group with the highest spending
highest_spending_age_group = age_group_spend.idxmax()

print(highest_spending_age_group)

