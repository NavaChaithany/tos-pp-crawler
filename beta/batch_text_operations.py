"""
batch_text_operations.py
Performs batch text operations across multiple records.
"""

import re

def convert_text_to_uppercase(records):
    """
    Convert text of each record to uppercase.
    """
    updated_records = []
    for record in records:
        updated = record.copy()
        updated['text'] = record.get('text', '').upper()
        updated_records.append(updated)
    return updated_records

def convert_text_to_lowercase(records):
    """
    Convert text of each record to lowercase.
    """
    updated_records = []
    for record in records:
        updated = record.copy()
        updated['text'] = record.get('text', '').lower()
        updated_records.append(updated)
    return updated_records

def convert_text_to_titlecase(records):
    """
    Convert text of each record to title case.
    """
    updated_records = []
    for record in records:
        updated = record.copy()
        updated['text'] = record.get('text', '').title()
        updated_records.append(updated)
    return updated_records

def strip_special_characters(records):
    """
    Remove non-alphanumeric characters from text.
    """
    updated_records = []
    for record in records:
        updated = record.copy()
        clean_text = re.sub(r'[^A-Za-z0-9\s]', '', record.get('text', ''))
        updated['text'] = clean_text
        updated_records.append(updated)
    return updated_records

def normalize_whitespace(records):
    """
    Normalize whitespace: remove multiple spaces.
    """
    updated_records = []
    for record in records:
        updated = record.copy()
        normalized_text = re.sub(r'\s+', ' ', record.get('text', '')).strip()
        updated['text'] = normalized_text
        updated_records.append(updated)
    return updated_records

def bulk_replace_keyword(records, old_word, new_word):
    """
    Replace a keyword with another in all records.
    """
    updated_records = []
    for record in records:
        updated = record.copy()
        replaced_text = record.get('text', '').replace(old_word, new_word)
        updated['text'] = replaced_text
        updated_records.append(updated)
    return updated_records

def count_keyword_occurrences_batch(records, keyword):
    """
    Count how many times a keyword appears across all records.
    """
    total_count = 0
    for record in records:
        text = record.get('text', '').lower()
        total_count += text.split().count(keyword.lower())
    return total_count

def apply_multiple_operations(records):
    """
    Apply a chain of operations: strip special characters, normalize, lower case.
    """
    print("\nApplying Batch Operations...")
    stripped = strip_special_characters(records)
    normalized = normalize_whitespace(stripped)
    lowered = convert_text_to_lowercase(normalized)
    return lowered

def simulate_batch_operations_run():
    """
    Simulate batch text operations on dummy records.
    """
    dummy_records = [
        {"title": "Doc 1", "text": "Hello! This is a Test TEXT. "},
        {"title": "Doc 2", "text": "Another @@ Example### with *** unwanted...characters!!!"}
    ]

    print("\nOriginal Records:")
    for rec in dummy_records:
        print(rec['text'])

    print("\nAfter Operations:")
    updated = apply_multiple_operations(dummy_records)
    for rec in updated:
        print(rec['text'])

    print("\nKeyword 'test' Occurrences:", count_keyword_occurrences_batch(updated, "test"))

