# case 6
# People in which segment are spending more money from the
# Monthly spend of each customer
import pandas as pd

# Assuming the data is stored in an Excel file named "Credit_Banking_Project1_part2.xlsx"
df = pd.read_excel("Credit_Banking_Project1_part2.xlsx")

# Grouping the data by customer_id and calculating the sum of spend for each customer
monthly_spend = df.groupby('Customer')['Amount_spend'].sum()

# Grouping the data by segment and calculating the sum of spend for each segment
segment_spend = df.groupby('Segment')['Amount_spend'].sum()

# Finding the highest spending segment
highest_spending_segment = segment_spend.idxmax()

# Print the highest spending segment
print(highest_spending_segment)
