python
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_excel('Trading_Summary_by_Investor_Type_March.xlsx')

# Display the first few rows of the dataset
print(data.head())

# Convert the date column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Group data by investor type and aggregate buy and sell values
grouped_data = data.groupby('Investor Type').agg({
    'Buy Value (AED)': 'sum',
    'Sell Value (AED)': 'sum',
    'Net Value (AED)': 'sum',
    'Buy Volume': 'sum',
    'Sell Volume': 'sum',
    'Net Volume': 'sum',
    'Buy Trades': 'sum',
    'Sell Trades': 'sum'
}).reset_index()

# Plot the buy and sell values by investor type
plt.figure(figsize=(10, 6))
grouped_data[['Investor Type', 'Buy Value (AED)', 'Sell Value (AED)']].set_index('Investor Type').plot(kind='bar')
plt.title('Buy and Sell Values by Investor Type in March 2026')
plt.xlabel('Investor Type')
plt.ylabel('Values in AED')
plt.show()

# Calculate daily net trading value
data['Daily Net Trading Value'] = data['Buy Value (AED)'] - data['Sell Value (AED)']

# Plot daily net trading values
plt.figure(figsize=(15, 8))
plt.plot(data['Date'], data['Daily Net Trading Value'], marker='o')
plt.title('Daily Net Trading Value in March 2026')
plt.xlabel('Date')
plt.ylabel('Net Trading Value (AED)')
plt.grid()
plt.show()

# Save aggregated data to a new Excel file
grouped_data.to_excel('Aggregated_Trading_Summary_March2026.xlsx', index=False)
