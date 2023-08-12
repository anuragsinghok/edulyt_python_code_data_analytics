# case 8
# Which is the most profitable segment
import pandas as pd

data = pd.read_excel("Project 1 part 4.xlsx")

# Grouping the data by segment and calculating the sum of profit/loss for each segment
segment_profit = data.groupby('Segment')['Profit / Loss'].sum()

# Finding the most profitable segment
most_profitable_segment = segment_profit[segment_profit == segment_profit.max()].index[0]

print(most_profitable_segment)

