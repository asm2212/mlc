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

def preprocess_data(df):
    """
    Preprocess the dataset.
    
    Parameters:
    - df: pd.DataFrame
        The input DataFrame.
    
    Returns:
    - X: pd.DataFrame
        The feature matrix.
    - y: pd.Series
        The target vector.
    """
    # Split the data into features and target
    X = df.drop('target', axis=1)
    y = df['target']
    
    return X, y

def split_data(X, y, test_size=0.2, random_state=42):
    """
    Split the data into training and testing sets.
    
    Parameters:
    - X: pd.DataFrame
        The feature matrix.
    - y: pd.Series
        The target vector.
    - test_size: float
        The proportion of the dataset to include in the test split.
    - random_state: int
        The seed used by the random number generator.
    
    Returns:
    - X_train, X_test, y_train, y_test: pd.DataFrame, pd.DataFrame, pd.Series, pd.Series
        The training and testing datasets.
    """
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

if __name__ == "__main__":
    # Load the data
    df = load_data('data/dataset.csv')
    
    # Preprocess the data
    X, y = preprocess_data(df)
    
    # Split the data
    X_train, X_test, y_train, y_test = split_data(X, y)
    
    # Save the processed data
    X_train.to_csv('data/X_train.csv', index=False)
    X_test.to_csv('data/X_test.csv', index=False)
    y_train.to_csv('data/y_train.csv', index=False)
    y_test.to_csv('data/y_test.csv', index=False)