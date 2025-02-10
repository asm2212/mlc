import pandas as pd

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', None, 'Eva'],
    'Age': [25, 30, 35, 40, 45, 30, 45],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Chicago', None],
    'BMI': [22.5, 24.0, 28.0, 26.5, 23.0, None, 23.0],
    'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', None, '2023-01-03', '2023-01-05']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# 1. Handle missing values
df['Name'].fillna('Unknown', inplace=True)
df['BMI'].fillna(df['BMI'].mean(), inplace=True)
df['City'].fillna('Unknown', inplace=True)
df['date'].fillna(method='ffill', inplace=True)

# 2. Remove duplicates
df.drop_duplicates(inplace=True)

# 3. Correct data types
df['date'] = pd.to_datetime(df['date'])

# Display the cleaned DataFrame
print("\nCleaned DataFrame:")
print(df)