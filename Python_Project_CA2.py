import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("CPI_GROUP.csv")
print(df.head(10))
'''
#checking data types and null values
print(df.info())

print(df.describe())

#checking misssing values
print(df.isnull().sum())
#checking duplicate rows
print(df.duplicated().sum())
print(df.drop_duplicates(inplace=True))


df['Inflation (%)']=df['Inflation (%)'].fillna(0)
print(df['Inflation (%)'])

df['SubGroup']=df['SubGroup'].replace("*","All Categories")
print(df['SubGroup'])

df['SubGroup'] = df['SubGroup'].str.strip()
print(df['SubGroup'])


df_sorted = df.sort_values(by='Inflation (%)', ascending=False)
print(df_sorted)

print(df['SubGroup'].unique())
print(df['Month'].value_counts())


print(df.dtypes)
df['Inflation (%)'] = pd.to_numeric(df['Inflation (%)'], errors='coerce')

# Group by Month and SubGroup, then calculate average Inflation
monthly_trend = df.groupby(['Month', 'SubGroup'])['Inflation (%)'].mean().reset_index()

# Plot
plt.figure(figsize=(14, 6))
sns.lineplot(data=monthly_trend, x='Month', y='Inflation (%)', hue='SubGroup')
plt.title('Monthly Inflation Trend by SubGroup')

plt.show()

'''



