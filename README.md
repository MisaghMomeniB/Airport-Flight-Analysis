# 📊 Airport Flights Data Analysis

This project provides a comprehensive analysis of flight data from various airports using Python libraries such as Pandas, Matplotlib, and Seaborn. The analysis includes data exploration, visualization, and correlation assessment.

## 📦 Dataset
The dataset (`airport_flights.csv`) contains the following columns:
- **Airport**: The name of the airport
- **Number of Flights**: The total number of flights for the period
- **Number of Passengers**: The total number of passengers
- **Amount**: Revenue generated by the airport

## 📈 Project Overview
### 1. Import Libraries and Load Data
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('airport_flights.csv')
```
The script imports necessary libraries and loads the dataset using Pandas.

### 2. Display Basic Information
```python
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
```
- **`head()`**: Displays the first five rows.
- **`info()`**: Provides data types and non-null counts.
- **`describe()`**: Summary statistics for numerical columns.
- **`isnull().sum()`**: Checks for missing values.

### 3. Key Metrics Calculation
```python
total_flights = df['Number of Flights'].sum()
total_passengers = df['Number of Passengers'].sum()
total_revenue = df['Amount'].sum()

print(f"Total Flights: {total_flights}")
print(f"Total Passengers: {total_passengers}")
print(f"Total Revenue: {total_revenue}")
```
Calculates the total number of flights, passengers, and revenue.

### 4. Data Visualization
#### Flights per Airport
```python
plt.figure(figsize=(10,6))
sns.barplot(x='Airport', y='Number of Flights', data=df)
plt.xticks(rotation=90)
plt.title('Number of Flights per Airport')
plt.show()
```
#### Passengers per Airport
```python
plt.figure(figsize=(10,6))
sns.barplot(x='Airport', y='Number of Passengers', data=df)
plt.xticks(rotation=90)
plt.title('Number of Passengers per Airport')
plt.show()
```
#### Revenue per Airport
```python
plt.figure(figsize=(10,6))
sns.barplot(x='Airport', y='Amount', data=df)
plt.xticks(rotation=90)
plt.title('Revenue per Airport')
plt.show()
```
### 5. Correlation Heatmap
```python
correlation_matrix = df[['Number of Flights', 'Amount', 'Number of Passengers']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
```
Visualizes the correlation between numeric columns to identify relationships.

## 🚀 How to Run the Project
1. Clone this repository.
2. Make sure you have Python installed along with Pandas, Matplotlib, and Seaborn:
   ```bash
   pip install pandas matplotlib seaborn
   ```
3. Run the script:
   ```bash
   python analysis.py
   ```

## 📊 Results
- Airports with the highest number of flights and passengers can be easily identified.
- Correlation heatmap shows the relationship between flights, passengers, and revenue.

## 🎯 Future Improvements
- Add time-series analysis for flight trends.
- Enhance visualizations with interactive plots.

## 📩 Contributing
Feel free to fork this project and submit pull requests!

## 📜 License
This project is licensed under the MIT License.

🌟 **Happy Analyzing!** 🌟
