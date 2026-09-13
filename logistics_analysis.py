import pandas as pd

# Load logistics data
data = pd.read_csv("logistics_data.csv")

# Basic exploration
print(data.head())
print(data.info())
print(data.describe())

# Check missing values
print(data.isnull().sum())

# Calculate average delivery time
average_delivery_time = data["delivery_time_hours"].mean()

print("Average Delivery Time:",
      average_delivery_time)
