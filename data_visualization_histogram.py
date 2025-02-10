import pandas as pd
import matplotlib.pyplot as plt

def create_histogram(df, column, bins, title, xlabel, ylabel, output_file):
    """
    Create a histogram for the specified column in the DataFrame and save it to a file.

    Parameters:
    - df: pd.DataFrame
      The input DataFrame containing numerical data.
    - column: str
      The column name to visualize using a histogram.
    - bins: int
      The number of bins for the histogram.
    - title: str
      The title of the histogram.
    - xlabel: str
      The label for the x-axis.
    - ylabel: str
      The label for the y-axis.
    - output_file: str
      The path to the file where the histogram will be saved.

    Returns:
    - None
    """
    # Create a histogram
    plt.figure(figsize=(10, 6))
    plt.hist(df[column], bins=bins, edgecolor='black')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # Save the plot to a file
    plt.savefig(output_file)
    print(f"Histogram saved to {output_file}")

# Example usage
if __name__ == "__main__":
    # Sample data
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace'],
        'Age': [25, 30, 35, 40, 45, 30, 50],
        'Score': [85, 90, 75, 92, 88, 85, 95]
    }

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Display the original DataFrame
    print("Original DataFrame:")
    print(df)

    # Create a histogram for the 'Age' column
    create_histogram(df, 'Age', bins=5, title='Age Distribution', xlabel='Age', ylabel='Frequency', output_file='age_histogram.png')

    # Create a histogram for the 'Score' column
    create_histogram(df, 'Score', bins=5, title='Score Distribution', xlabel='Score', ylabel='Frequency', output_file='score_histogram.png')