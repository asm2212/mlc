import pandas as pd
from sklearn.feature_selection import SelectKBest, chi2, RFE
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.linear_model import LogisticRegression

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

def univariate_selection(X, y):
    """
    Perform univariate feature selection.
    
    Parameters:
    - X: pd.DataFrame
        The feature matrix.
    - y: pd.Series
        The target vector.
    
    Returns:
    - pd.DataFrame
        The scores of each feature.
    """
    selector = SelectKBest(score_func=chi2, k='all')
    fit = selector.fit(X, y)
    scores = pd.DataFrame(fit.scores_, index=X.columns, columns=['Score'])
    return scores

def recursive_feature_elimination(X, y):
    """
    Perform recursive feature elimination.
    
    Parameters:
    - X: pd.DataFrame
        The feature matrix.
    - y: pd.Series
        The target vector.
    
    Returns:
    - list
        The ranking of each feature.
    """
    model = LogisticRegression(solver='liblinear')
    selector = RFE(model, n_features_to_select=1)
    fit = selector.fit(X, y)
    rankings = pd.DataFrame(fit.ranking_, index=X.columns, columns=['Ranking'])
    return rankings

def feature_importance(X, y):
    """
    Perform feature importance ranking using tree-based method.
    
    Parameters:
    - X: pd.DataFrame
        The feature matrix.
    - y: pd.Series
        The target vector.
    
    Returns:
    - pd.DataFrame
        The importance of each feature.
    """
    model = ExtraTreesClassifier()
    model.fit(X, y)
    importances = pd.DataFrame(model.feature_importances_, index=X.columns, columns=['Importance'])
    return importances

if __name__ == "__main__":
    # Load the data
    df = load_data('data/dataset.csv')
    
    # Split the data into features and target
    X = df.drop('target', axis=1)
    y = df['target']
    
    # Perform univariate selection
    univariate_scores = univariate_selection(X, y)
    print("Univariate Selection Scores:")
    print(univariate_scores)
    
    # Perform recursive feature elimination
    rfe_rankings = recursive_feature_elimination(X, y)
    print("\nRecursive Feature Elimination Rankings:")
    print(rfe_rankings)
    
    # Perform feature importance ranking
    importance_scores = feature_importance(X, y)
    print("\nFeature Importance Scores:")
    print(importance_scores)