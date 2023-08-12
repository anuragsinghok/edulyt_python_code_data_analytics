# case 9
# which category the customers are spending more money
import pandas as pd

data = pd.read_excel("Project 1 part 3.xlsx")

# Grouping the data by category and calculating the sum of total amount spend for each category
category_totals = data.groupby('Category')['Total amount spend'].sum()

# Finding the category with the highest total amount spend
highest_spending_categories = category_totals[category_totals == category_totals.max()].index.tolist()

print(highest_spending_categories)
