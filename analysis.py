# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('airport_flights.csv')

print(df.head())

print(df.info())  # Data types and non-null counts
print(df.describe())  # Summary statistics for numeric columns

print(df.isnull().sum())

total_flights = df['Number of Flights'].sum()
total_passengers = df['Number of Passengers'].sum()
total_revenue = df['Amount'].sum()

print(f"Total Flights: {total_flights}")
print(f"Total Passengers: {total_passengers}")
print(f"Total Revenue: {total_revenue}")

plt.figure(figsize=(10,6))
sns.barplot(x='Airport', y='Number of Flights', data=df)
plt.xticks(rotation=90)
plt.title('Number of Flights per Airport')
plt.show()

plt.figure(figsize=(10,6))
sns.barplot(x='Airport', y='Number of Passengers', data=df)
plt.xticks(rotation=90)
plt.title('Number of Passengers per Airport')
plt.show()

plt.figure(figsize=(10,6))
sns.barplot(x='Airport', y='Amount', data=df)
plt.xticks(rotation=90)
plt.title('Revenue per Airport')
plt.show()

correlation_matrix = df[['Number of Flights', 'Amount', 'Number of Passengers']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()