"""
file_utils.py
Utility functions for file operations.
"""

import json

def load_json_file(filepath):
    """
    Loads a JSON file from the given filepath.

    Args:
        filepath (str): Path to the JSON file.

    Returns:
        list: Loaded JSON data as a list of dictionaries.
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def save_json_file(data, filepath):
    """
    Saves data into a JSON file.

    Args:
        data (list): List of dictionaries to save.
        filepath (str): Path to save the file.
    """
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def append_json_file(new_data, filepath):
    """
    Appends new records to an existing JSON file.

    Args:
        new_data (list): New list of dictionaries.
        filepath (str): Existing JSON file path.
    """
    existing_data = load_json_file(filepath)
    combined_data = existing_data + new_data
    save_json_file(combined_data, filepath)
