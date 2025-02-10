import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(filepath):
    """
    Load the dataset from a CSV file.
    
    Parameters:
    - filepath: str
        The path to the CSV file.
    
    Returns:
    - pd.DataFrame
        The loaded DataFrame.
    """
    return pd.read_csv(filepath)

def split_data(df, test_size=0.2, random_state=42):
    """
    Split the dataset into training and testing sets.
    
    Parameters:
    - df: pd.DataFrame
        The input DataFrame.
    - test_size: float
        The proportion of the dataset to include in the test split.
    - random_state: int
        The seed used by the random number generator.
    
    Returns:
    - pd.DataFrame, pd.DataFrame, pd.Series, pd.Series
        The training and testing feature matrices and target vectors.
    """
    X = df.drop('target', axis=1)
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test

def save_data(X_train, X_test, y_train, y_test, output_dir='data/'):
    """
    Save the training and testing datasets to CSV files.
    
    Parameters:
    - X_train: pd.DataFrame
        The training feature matrix.
    - X_test: pd.DataFrame
        The testing feature matrix.
    - y_train: pd.Series
        The training target vector.
    - y_test: pd.Series
        The testing target vector.
    - output_dir: str
        The directory where the CSV files will be saved.
    
    Returns:
    - None
    """
    X_train.to_csv(f'{output_dir}X_train.csv', index=False)
    X_test.to_csv(f'{output_dir}X_test.csv', index=False)
    y_train.to_csv(f'{output_dir}y_train.csv', index=False)
    y_test.to_csv(f'{output_dir}y_test.csv', index=False)
    print(f"Data saved to {output_dir}")

if __name__ == "__main__":
    # Load the data
    df = load_data('data/dataset.csv')
    
    # Split the data
    X_train, X_test, y_train, y_test = split_data(df)
    
    # Save the split data
    save_data(X_train, X_test, y_train, y_test)