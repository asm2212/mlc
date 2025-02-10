import pandas as pd
from sklearn.preprocessing import LabelEncoder

def label_encode_columns(df, columns):
    """
    Label encode the specified columns in the DataFrame.

    Parameters:
    - df: pd.DataFrame
      The input DataFrame with categorical columns to be encoded.
    - columns: list
      A list of column names to be label encoded.

    Returns:
    - pd.DataFrame
      The DataFrame with label encoded columns.
    - dict
      A dictionary mapping original labels to encoded labels for each column.
    """
    label_encoders = {}
    for column in columns:           
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
        label_encoders[column] = dict(zip(le.classes_, le.transform(le.classes_)))
    return df, label_encoders

# Example usage
if __name__ == "__main__":
    # Sample data
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
        'Occupation': ['Engineer', 'Doctor', 'Teacher', 'Lawyer', 'Artist']
    }

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Display the original DataFrame
    print("Original DataFrame:")
    print(df)

    # Columns to be label encoded
    columns_to_encode = ['City', 'Occupation']

    # Label encode the columns
    encoded_df, label_mappings = label_encode_columns(df, columns_to_encode)

    # Display the encoded DataFrame
    print("\nEncoded DataFrame:")
    print(encoded_df)

    # Display the label mappings
    print("\nLabel Mappings:")
    for column, mapping in label_mappings.items():
        print(f"{column}: {mapping}")