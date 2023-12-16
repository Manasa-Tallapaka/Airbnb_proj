# utils/data_handler.py

import pandas as pd

# Example data loading method
def load_data(file_path):
    """
    Load data from a CSV file using pandas.

    Parameters:
    - file_path (str): The path to the CSV file.

    Returns:
    - DataFrame: A pandas DataFrame containing the loaded data.
    """
    # Use pandas to read the CSV file into a DataFrame
    data = pd.read_csv("C:\Users\talla\Downloads\airbnb_proj\airbnb.csv")
    return data

# Example data preprocessing method
def preprocess_data(data):

    return data

# Example data saving method
def save_data(data, output_file):
  
    # Use pandas to save the DataFrame to a CSV file
    data.to_csv(output_file, index=False)
    print(f"Data saved to {output_file}")
