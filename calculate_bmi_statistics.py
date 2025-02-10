import pandas as pd

def calculate_bmi_statistics(df, bmi_column):
    """
    Calculate the mean, median, and variance of BMI from the given DataFrame.

    Parameters:
    - df: pd.DataFrame
        The input DataFrame containing BMI data.
    - bmi_column: str
        The name of the column in the DataFrame that contains BMI values.

    Returns:
    - dict
        A dictionary containing the mean, median, and variance of BMI.
    """
    mean_bmi = df[bmi_column].mean()
    median_bmi = df[bmi_column].median()
    variance_bmi = df[bmi_column].var()

    return {
        'mean_bmi': mean_bmi,
        'median_bmi': median_bmi,
        'variance_bmi': variance_bmi
    }

# Example usage
if __name__ == "__main__":
    # Sample data
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Age': [25, 30, 35, 40, 45],
        'BMI': [22.5, 24.0, 28.0, 26.5, 23.0]
    }

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Calculate BMI statistics
    bmi_stats = calculate_bmi_statistics(df, 'BMI')

    # Display the results
    print("BMI Statistics:")
    print(f"Mean BMI: {bmi_stats['mean_bmi']}")
    print(f"Median BMI: {bmi_stats['median_bmi']}")
    print(f"Variance BMI: {bmi_stats['variance_bmi']}")