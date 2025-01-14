import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine
import os

# Step 1: Data Ingestion
# Prompt the user for the correct file path if the file is not found
data_file = 'RBI_Daily_Digital_Payments_Sample_Data.csv'

if not os.path.exists(data_file):
    print(f"The file '{data_file}' does not exist in the current directory: {os.getcwd()}")
    data_file = input("Please enter the full path to the data file: ").strip()
    if not os.path.exists(data_file):
        raise FileNotFoundError(f"The file '{data_file}' does not exist. Please provide a valid path.")

# Load the data from the provided CSV file
data = pd.read_csv(data_file)


# Load the data from the provided CSV file
data = pd.read_csv(data_file)

# Step 2: Data Transformation
# Normalize column names
data.columns = [col.strip().lower().replace(' ', '_') for col in data.columns]

# Convert date columns to datetime if applicable (example: assuming a 'date' column exists)
if 'date' in data.columns:
    data['date'] = pd.to_datetime(data['date'], errors='coerce')

# Handle missing values
data.fillna(0, inplace=True)

# Derive new metrics (example: total transactions if 'transactions' and 'volume' exist)
if 'transactions' in data.columns and 'volume' in data.columns:
    data['transactions_per_volume'] = data['transactions'] / data['volume']

# Step 3: Data Storage
# Create a SQLite database to store processed data
engine = create_engine('sqlite:///digital_payments.db')
data.to_sql('digital_payments', engine, if_exists='replace', index=False)

# Step 4: Data Analysis and Visualization
# Analyze trends
if 'date' in data.columns and 'transactions' in data.columns:
    daily_trends = data.groupby('date')['transactions'].sum().reset_index()

    # Plot daily transactions
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=daily_trends, x='date', y='transactions', marker='o')
    plt.title('Daily Transactions Trend')
    plt.xlabel('Date')
    plt.ylabel('Transactions')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('daily_transactions_trend.png')
    plt.show()

# Step 5: Automation
# Example placeholder: Automate with Airflow or Prefect (not implemented in this script)
# Define tasks and workflows for automation

# Print completion message
print("Pipeline executed successfully. Processed data is stored in 'digital_payments.db', and visualization is saved as 'daily_transactions_trend.png'.")
