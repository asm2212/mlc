import pandas as pd

def calculate_sta(data, stroke):
    """
    Calculate the mean, median, and variance of BMI for stroke patients.

    Parameters:
    - data: pd.DataFrame
        The input DataFrame containing BMI data.
    - stroke: str
        The column name indicating stroke status.

    Returns:
    - dict
        A dictionary containing the mean, median, and variance of BMI for stroke patients.
    """
    # Filter the data for stroke patients
    df = data[data[stroke] == 1]
    
    # Calculate statistics
    mean = df['bmi'].mean()
    median = df['bmi'].median()
    variance = df['bmi'].var()
    
    # Store the statistics in a dictionary
    stat = {
        'mean': mean,
        'median': median,
        'variance': variance
    }
    
    return stat

# Example usage
if __name__ == "__main__":
    # Sample data
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Age': [25, 30, 35, 40, 45],
        'BMI': [22.5, 24.0, 28.0, 26.5, 23.0],
        'stroke': [0, 1, 0, 1, 0]
    }

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Calculate BMI statistics for stroke patients
    bmi_stats = calculate_sta(df, 'stroke')

    # Display the results
    print("BMI Statistics for Stroke Patients:")
    print(f"Mean BMI: {bmi_stats['mean']}")
    print(f"Median BMI: {bmi_stats['median']}")
    print(f"Variance BMI: {bmi_stats['variance']}")