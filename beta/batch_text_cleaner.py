"""
batch_text_cleaner.py
Provides text cleaning utilities for batch processing.
"""

import re
import unicodedata

def remove_html_tags(text):
    """
    Remove HTML tags using regex.
    """
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def remove_javascript(text):
    """
    Remove JavaScript code patterns.
    """
    text = re.sub(r'<script.*?>.*?</script>', '', text, flags=re.DOTALL)
    text = re.sub(r'window\..*?;', '', text)
    return text

def remove_special_characters(text):
    """
    Remove special characters except basic punctuation.
    """
    return re.sub(r'[^A-Za-z0-9\s.,!?]', '', text)

def normalize_unicode(text):
    """
    Normalize unicode to NFKC form.
    """
    return unicodedata.normalize('NFKC', text)

def basic_text_cleaner(text):
    """
    Apply a chain of basic text cleaning steps.
    """
    text = normalize_unicode(text)
    text = remove_html_tags(text)
    text = remove_javascript(text)
    text = remove_special_characters(text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def clean_batch_texts(records):
    """
    Clean text field for a batch of records.
    """
    cleaned = []
    for record in records:
        updated = record.copy()
        updated['text'] = basic_text_cleaner(record.get('text', ''))
        cleaned.append(updated)
    return cleaned

def simulate_batch_cleaning_run():
    """
    Simulate cleaning of dummy batch records.
    """
    dummy_records = [
        {"title": "Doc X", "text": "<html><body>Hello <script>alert('hi')</script> World!!</body></html>"},
        {"title": "Doc Y", "text": "window.alert('test'); Special *** characters ## everywhere!!!"}
    ]

    cleaned = clean_batch_texts(dummy_records)

    print("\nCleaned Records:")
    for rec in cleaned:
        print(rec['text'])

