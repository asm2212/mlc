import pandas as pd

def load_and_merge_data(filepaths, merge_on):
    """
    Load and merge multiple CSV files into a single DataFrame.

    Parameters:
    - filepaths: list
      A list of file paths to the CSV files.
    - merge_on: str
      The column name to merge the DataFrames on.

    Returns:
    - pd.DataFrame
      The merged DataFrame.
    """
    data_frames = [pd.read_csv(filepath) for filepath in filepaths]
    merged_df = data_frames[0]
    
    for df in data_frames[1:]:
        merged_df = pd.merge(merged_df, df, on=merge_on, how='outer')
    
    return merged_df

def main():
    # File paths to the CSV files
    filepaths = ['data1.csv', 'data2.csv', 'data3.csv']
    
    # The column to merge on
    merge_on = 'ID'
    
    # Load and merge the data
    merged_df = load_and_merge_data(filepaths, merge_on)
    
    # Display the merged DataFrame
    print("Merged DataFrame:")
    print(merged_df)

    # Perform some analysis on the merged data
    print("\nSummary Statistics:")
    print(merged_df.describe())
    
    # Save the merged DataFrame to a new CSV file
    merged_df.to_csv('merged_data.csv', index=False)
    print("\nMerged data has been saved to 'merged_data.csv'.")

if __name__ == "__main__":
    main()