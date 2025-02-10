import pandas as pd

def clean_data(df):
    """
    Clean the input DataFrame by performing the following operations:
    1. Handle missing values.
    2. Remove duplicates.
    3. Correct data types.
    
    Parameters:
    - df: pd.DataFrame
        The input DataFrame to be cleaned.
    
    Returns:
    - pd.DataFrame
        The cleaned DataFrame.
    """
    # 1. Handle missing values
    # Fill missing numeric values with the mean of the column
    for col in df.select_dtypes(include='number').columns:
        df[col].fillna(df[col].mean(), inplace=True)
    
    # Fill missing categorical values with the mode of the column
    for col in df.select_dtypes(include='object').columns:
        df[col].fillna(df[col].mode()[0], inplace=True)
    
    # 2. Remove duplicates
    df.drop_duplicates(inplace=True)
    
    # 3. Correct data types
    # Convert columns to appropriate data types
    # For example, convert 'date' column to datetime
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])
    
    # Convert categorical columns to category data type
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].astype('category')
    
    return df

# Example usage
if __name__ == "__main__":
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

    # Clean the data
    cleaned_df = clean_data(df)

    # Display the cleaned DataFrame
    print("\nCleaned DataFrame:")
    print(cleaned_df)