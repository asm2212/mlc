import pandas as pd

def load_data(filepaths):
    """
    Load multiple CSV files into DataFrames.

    Parameters:
    - filepaths: list
      A list of file paths to the CSV files.

    Returns:
    - list
      A list of DataFrames.
    """
    return [pd.read_csv(filepath) for filepath in filepaths]

def left_join(df1, df2, on):
    """
    Perform a left join on two DataFrames.

    Parameters:
    - df1: pd.DataFrame
      The left DataFrame.
    - df2: pd.DataFrame
      The right DataFrame.
    - on: str
      The column name to join on.

    Returns:
    - pd.DataFrame
      The resulting DataFrame after the left join.
    """
    return pd.merge(df1, df2, on=on, how='left')

def right_join(df1, df2, on):
    """
    Perform a right join on two DataFrames.

    Parameters:
    - df1: pd.DataFrame
      The left DataFrame.
    - df2: pd.DataFrame
      The right DataFrame.
    - on: str
      The column name to join on.

    Returns:
    - pd.DataFrame
      The resulting DataFrame after the right join.
    """
    return pd.merge(df1, df2, on=on, how='right')

def main():
    # File paths to the CSV files
    filepaths = ['data1.csv', 'data2.csv']
    
    # Load the data
    df1, df2 = load_data(filepaths)
    
    # Perform left join
    left_joined_df = left_join(df1, df2, on='ID')
    print("Left Join Result:")
    print(left_joined_df)
    
    # Perform right join
    right_joined_df = right_join(df1, df2, on='ID')
    print("\nRight Join Result:")
    print(right_joined_df)

if __name__ == "__main__":
    main()