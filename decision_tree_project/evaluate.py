import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

def load_data():
    """
    Load the testing data.
    
    Returns:
    - X_test, y_test: pd.DataFrame, pd.Series
        The testing datasets.
    """
    X_test = pd.read_csv('data/X_test.csv')
    y_test = pd.read_csv('data/y_test.csv').squeeze()  # Convert to Series
    
    return X_test, y_test

def load_model(filepath):
    """
    Load a trained model from a file.
    
    Parameters:
    - filepath: str
        The path to the file where the model is saved.
    
    Returns:
    - model: DecisionTreeClassifier
        The loaded model.
    """
    return joblib.load(filepath)

def evaluate_model(model, X_test, y_test):
    """
    Evaluate the trained model on the testing data.
    
    Parameters:
    - model: DecisionTreeClassifier
        The trained model.
    - X_test: pd.DataFrame
        The feature matrix for testing.
    - y_test: pd.Series
        The target vector for testing.
    
    Returns:
    - None
    """
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')
    cm = confusion_matrix(y_test, y_pred)
    
    print(f"Accuracy: {accuracy}")
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")
    print(f"F1 Score: {f1}")
    print(f"Confusion Matrix:\n{cm}")

if __name__ == "__main__":
    # Load the data
    X_test, y_test = load_data()
    
    # Load the model
    model = load_model('models/decision_tree_model.pkl')
    
    # Evaluate the model
    evaluate_model(model, X_test, y_test)