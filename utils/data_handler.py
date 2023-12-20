import json
import pandas as pd

def read_data(file_path):
    """
    Read data from a JSON file.

    Parameters:
    - file_path (str): The path to the JSON file.

    Returns:
    - list: A list containing the loaded data.
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def write_data(file_path, data):
    """
    Write data to a JSON file.

    Parameters:
    - file_path (str): The path to the JSON file.
    - data (list): The data to be written.

    Returns:
    - None
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

# Example data loading method for CSV (you may need to adjust this based on your needs)
def load_data_csv(file_path):
    """
    Load data from a CSV file using pandas.

    Parameters:
    - file_path (str): The path to the CSV file.

    Returns:
    - DataFrame: A pandas DataFrame containing the loaded data.
    """
    # Use pandas to read the CSV file into a DataFrame
    data = pd.read_csv(file_path)
    return data

# Example data preprocessing method (you can modify this based on your actual preprocessing needs)
def preprocess_data(data):
    return data

# Example data saving method for CSV (you may need to adjust this based on your needs)
def save_data_csv(data, output_file):
    """
    Save data to a CSV file using pandas.

    Parameters:
    - data (DataFrame): The data to be saved.
    - output_file (str): The path to the output CSV file.

    Returns:
    - None
    """
    # Use pandas to save the DataFrame to a CSV file
    data.to_csv(output_file, index=False)
    print(f"Data saved to {output_file}")
