# provide a meaningful treatment to all values where age is less than 18 
import pandas as pd

# Assuming the data is stored in a CSV file named "data.csv"
df = pd.read_csv("Credit Banking_Project1.csv")


df['Treatment'] = df.loc[df['Age'] < 18, 'Treatment'].fillna('Underage Treatment')

# Print the updated dataset
print(df)

