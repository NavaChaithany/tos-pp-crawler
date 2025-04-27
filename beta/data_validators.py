"""
data_validators.py
Simple validation utilities for checking scraped or simulated data records.
"""

def validate_record_structure(record):
    """
    Validates if the record contains mandatory fields: title, url, and text.

    Args:
        record (dict): A single record dictionary.

    Returns:
        bool: True if valid, False otherwise.
    """
    required_fields = ['title', 'url', 'text']
    for field in required_fields:
        if field not in record or not record[field].strip():
            return False
    return True

def validate_dataset(dataset):
    """
    Validates an entire dataset.

    Args:
        dataset (list): List of record dictionaries.

    Returns:
        tuple: (number of valid records, number of invalid records)
    """
    valid = 0
    invalid = 0
    for record in dataset:
        if validate_record_structure(record):
            valid += 1
        else:
            invalid += 1
    return valid, invalid

def summarize_validation(dataset):
    """
    Prints a simple validation report.

    Args:
        dataset (list): List of record dictionaries.
    """
    valid, invalid = validate_dataset(dataset)
    total = valid + invalid
    print(f"Validation Summary:")
    print(f"Total records: {total}")
    print(f"Valid records: {valid}")
    print(f"Invalid records: {invalid}")
    if invalid > 0:
        print("Warning: Some records are missing fields.")
