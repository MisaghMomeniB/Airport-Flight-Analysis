# Import necessary libraries
import pandas as pd  # pandas is for data manipulation and analysis
import matplotlib.pyplot as plt  # matplotlib is for plotting graphs
import seaborn as sns  # seaborn is a statistical data visualization library

# Load the dataset from a CSV file
df = pd.read_csv('airport_flights.csv')  # Read CSV file into a DataFrame

# Display the first 5 rows of the DataFrame to understand its structure
print(df.head())  # Shows the first 5 rows of the data

# Display basic info about the DataFrame, including column data types and non-null counts
print(df.info())  # Information about the DataFrame, including datatypes and missing values

# Generate summary statistics (mean, std, min, 25%, 50%, 75%, max) for numerical columns
print(df.describe())  # Provides summary statistics for numerical columns

# Count the number of missing (null) values in each column
print(df.isnull().sum())  # Count of missing values for each column

# Calculate the total number of flights from the 'Number of Flights' column
total_flights = df['Number of Flights'].sum()  # Sum of all the flight counts
# Calculate the total number of passengers from the 'Number of Passengers' column
total_passengers = df['Number of Passengers'].sum()  # Sum of all passenger counts
# Calculate the total revenue from the 'Amount' column
total_revenue = df['Amount'].sum()  # Sum of all revenue amounts

# Print the total number of flights, passengers, and revenue
print(f"Total Flights: {total_flights}")  # Display total number of flights
print(f"Total Passengers: {total_passengers}")  # Display total number of passengers
print(f"Total Revenue: {total_revenue}")  # Display total revenue

# Create a bar plot for the number of flights per airport
plt.figure(figsize=(10,6))  # Set the figure size for the plot
sns.barplot(x='Airport', y='Number of Flights', data=df)  # Create a bar plot using seaborn
plt.xticks(rotation=90)  # Rotate x-axis labels (airport names) for better readability
plt.title('Number of Flights per Airport')  # Title of the plot
plt.show()  # Show the plot

# Create a bar plot for the number of passengers per airport
plt.figure(figsize=(10,6))  # Set the figure size for the plot
sns.barplot(x='Airport', y='Number of Passengers', data=df)  # Create a bar plot for passengers
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
plt.title('Number of Passengers per Airport')  # Title of the plot
plt.show()  # Show the plot

# Create a bar plot for the revenue per airport
plt.figure(figsize=(10,6))  # Set the figure size for the plot
sns.barplot(x='Airport', y='Amount', data=df)  # Create a bar plot for revenue
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
plt.title('Revenue per Airport')  # Title of the plot
plt.show()  # Show the plot

# Compute the correlation matrix for the selected numerical columns
correlation_matrix = df[['Number of Flights', 'Amount', 'Number of Passengers']].corr()  # Calculate correlation matrix

# Create a heatmap to visualize the correlation matrix
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')  # Generate the heatmap with annotations
plt.title('Correlation Heatmap')  # Title of the heatmap
plt.show()  # Display the heatmap