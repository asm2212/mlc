import pandas as pd
import numpy as np

def interpolate_numerical_columns(df):
    """
    Interpolate missing values in numerical columns using linear interpolation.

    Parameters:
    - df: pd.DataFrame
        The input DataFrame with potential missing values in numerical columns.

    Returns:
    - pd.DataFrame
        The DataFrame with interpolated values in numerical columns.
    """
    # Apply linear interpolation to numerical columns
    df.interpolate(method='linear', inplace=True)
    
    # Fill any remaining NaNs with the mean of the column (if interpolation fails)
    for col in df.select_dtypes(include=np.number).columns:
        df[col].fillna(df[col].mean(), inplace=True)
    
    return df

# Example usage
if __name__ == "__main__":
    # Sample data with missing values
    data = {
        'Time': [1, 2, 3, 4, 5],
        'Temperature': [22.5, np.nan, 27.0, np.nan, 23.0],
        'Pressure': [1012, 1013, np.nan, 1015, np.nan]
    }

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Display the original DataFrame
    print("Original DataFrame:")
    print(df)

    # Interpolate missing values in numerical columns
    interpolated_df = interpolate_numerical_columns(df)

    # Display the DataFrame with interpolated values
    print("\nDataFrame after Linear Interpolation:")
    print(interpolated_df)