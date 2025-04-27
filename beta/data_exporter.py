"""
data_exporter.py
Provides utilities to export crawled data into different formats.
"""

import json
import csv
import os

def export_to_csv(records, filename='export.csv'):
    """
    Export records to a CSV file.
    """
    if not records:
        print("No records to export.")
        return

    fieldnames = ['title', 'url', 'text']

    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for record in records:
            writer.writerow({
                'title': record.get('title', ''),
                'url': record.get('url', ''),
                'text': record.get('text', '')
            })
    print(f"Exported {len(records)} records to {filename}")

def export_to_jsonl(records, filename='export.jsonl'):
    """
    Export records to JSON lines file.
    """
    if not records:
        print("No records to export.")
        return

    with open(filename, 'w', encoding='utf-8') as f:
        for record in records:
            f.write(json.dumps(record) + '\n')
    print(f"Exported {len(records)} records to {filename}")

def export_texts_to_txt(records, directory='texts'):
    """
    Export each text to a separate .txt file.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

    for idx, record in enumerate(records):
        title = record.get('title', f'document_{idx}')
        safe_title = title.replace(' ', '_').replace('/', '_')
        filename = os.path.join(directory, f"{safe_title}.txt")
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(record.get('text', ''))
    print(f"Exported {len(records)} text files to {directory}/")

def validate_file_exists(filename):
    """
    Validate that a file exists.
    """
    exists = os.path.exists(filename)
    print(f"File {filename} exists: {exists}")
    return exists

def validate_directory_exists(directory):
    """
    Validate that a directory exists.
    """
    exists = os.path.isdir(directory)
    print(f"Directory {directory} exists: {exists}")
    return exists

def simulate_export_process():
    """
    Simulate export of dummy records.
    """
    dummy_records = [
        {"title": f"Document {i}", "url": f"https://example.com/{i}", "text": f"Sample text content {i}."}
        for i in range(10)
    ]

    print("\nSimulating CSV export...")
    export_to_csv(dummy_records, filename='dummy_export.csv')
    validate_file_exists('dummy_export.csv')

    print("\nSimulating JSONL export...")
    export_to_jsonl(dummy_records, filename='dummy_export.jsonl')
    validate_file_exists('dummy_export.jsonl')

    print("\nSimulating TXT export...")
    export_texts_to_txt(dummy_records, directory='dummy_texts')
    validate_directory_exists('dummy_texts')
