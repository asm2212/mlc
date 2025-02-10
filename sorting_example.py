import pandas as pd

def sort_dataframe(df, sort_columns, ascending=True):
    """
    Sort the DataFrame by the specified columns.

    Parameters:
    - df: pd.DataFrame
      The input DataFrame to be sorted.
    - sort_columns: list
      A list of column names to sort by.
    - ascending: bool or list of bool, default True
      Sort ascending vs. descending. When the list is used, it should match the length of sort_columns.

    Returns:
    - pd.DataFrame
      The sorted DataFrame.
    """
    sorted_df = df.sort_values(by=sort_columns, ascending=ascending)
    return sorted_df

# Example usage
if __name__ == "__main__":
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

    # Sort the DataFrame by 'Age' in ascending order
    sorted_df_age = sort_dataframe(df, ['Age'])
    print("\nDataFrame sorted by 'Age' in ascending order:")
    print(sorted_df_age)

    # Sort the DataFrame by 'Score' in descending order
    sorted_df_score_desc = sort_dataframe(df, ['Score'], ascending=False)
    print("\nDataFrame sorted by 'Score' in descending order:")
    print(sorted_df_score_desc)

    # Sort the DataFrame by 'City' and then by 'Age' in ascending order
    sorted_df_city_age = sort_dataframe(df, ['City', 'Age'])
    print("\nDataFrame sorted by 'City' and then by 'Age' in ascending order:")
    print(sorted_df_city_age)