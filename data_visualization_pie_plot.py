import pandas as pd
import matplotlib.pyplot as plt

def create_pie_plot(df, column, title, output_file):
    """
    Create a pie plot for the specified column in the DataFrame and save it to a file.

    Parameters:
    - df: pd.DataFrame
      The input DataFrame containing categorical data.
    - column: str
      The column name to visualize using a pie plot.
    - title: str
      The title of the pie plot.
    - output_file: str
      The path to the file where the pie plot will be saved.

    Returns:
    - None
    """
    # Get the value counts for the specified column
    data = df[column].value_counts()

    # Create a pie plot
    plt.figure(figsize=(8, 8))
    plt.pie(data, labels=data.index, autopct='%1.1f%%', startangle=140)
    plt.title(title)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Save the plot to a file
    plt.savefig(output_file)
    print(f"Pie plot saved to {output_file}")

# Example usage
if __name__ == "__main__":
    # Sample data
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace'],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Chicago', 'Houston'],
    }

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Display the original DataFrame
    print("Original DataFrame:")
    print(df)

    # Create a pie plot for the 'City' column
    create_pie_plot(df, 'City', 'City Distribution', 'city_distribution_pie_plot.png')