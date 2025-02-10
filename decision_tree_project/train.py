import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

def load_data():
    """
    Load the training and testing data.
    
    Returns:
    - X_train, X_test, y_train, y_test: pd.DataFrame, pd.DataFrame, pd.Series, pd.Series
        The training and testing datasets.
    """
    X_train = pd.read_csv('data/X_train.csv')
    X_test = pd.read_csv('data/X_test.csv')
    y_train = pd.read_csv('data/y_train.csv').squeeze()  # Convert to Series
    y_test = pd.read_csv('data/y_test.csv').squeeze()  # Convert to Series
    
    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):
    """
    Train a decision tree classifier.
    
    Parameters:
    - X_train: pd.DataFrame
        The feature matrix for training.
    - y_train: pd.Series
        The target vector for training.
    
    Returns:
    - model: DecisionTreeClassifier
        The trained model.
    """
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)
    
    return model

def save_model(model, filepath):
    """
    Save the trained model to a file.
    
    Parameters:
    - model: DecisionTreeClassifier
        The trained model.
    - filepath: str
        The path to the file where the model will be saved.
    
    Returns:
    - None
    """
    joblib.dump(model, filepath)
    print(f"Model saved to {filepath}")

if __name__ == "__main__":
    # Load the data
    X_train, X_test, y_train, y_test = load_data()
    
    # Train the model
    model = train_model(X_train, y_train)
    
    # Save the model
    save_model(model, 'models/decision_tree_model.pkl')