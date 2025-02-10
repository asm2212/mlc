import pandas as pd

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Score': [85, 90, 75, 92, 88]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Filter rows where Age is greater than 30
filtered_df = df[df['Age'] > 30]

# Display the filtered DataFrame
print("\nFiltered DataFrame (Age > 30):")
print(filtered_df)

# Filter rows where City is 'Chicago'
filtered_df_city = df[df['City'] == 'Chicago']

# Display the filtered DataFrame
print("\nFiltered DataFrame (City is 'Chicago'):")
print(filtered_df_city)

# Filter rows using query method (Score greater than 80)
filtered_df_query = df.query('Score > 80')

# Display the filtered DataFrame
print("\nFiltered DataFrame (Score > 80 using query method):")
print(filtered_df_query)

# Filter rows using loc (Age between 30 and 40)
filtered_df_loc = df.loc[(df['Age'] >= 30) & (df['Age'] <= 40)]

# Display the filtered DataFrame
print("\nFiltered DataFrame (Age between 30 and 40 using loc):")
print(filtered_df_loc)