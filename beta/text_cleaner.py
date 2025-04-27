"""
text_cleaner.py
Functions to clean raw scraped text data.
"""

import re

def clean_text(text):
    """
    Cleans the input text by removing unwanted patterns like JavaScript, CSS, 
    meta fields, numbers, extra spaces, and non-ASCII characters.

    Args:
        text (str): Raw scraped text.

    Returns:
        str: Cleaned text.
    """
    # Remove window object assignments
    text = re.sub(r'window\..*?;', '', text)

    # Remove function definitions
    text = re.sub(r'function\s*\(.*?\)\s*{.*?}', '', text, flags=re.DOTALL)

    # Remove JSON-like { ... } and [ ... ] artifacts
    text = re.sub(r'\{.*?\}', '', text, flags=re.DOTALL)
    text = re.sub(r'\[.*?\]', '', text, flags=re.DOTALL)

    # Remove "key": "value" pairs often present in JS configs
    text = re.sub(r'\"[^\"]*\"\s*:\s*\"[^\"]*\"', '', text)
    text = re.sub(r'\"[^\"]*\"\s*:\s*[^,]*,?', '', text)

    # Remove .graphql, .react, .rendererRef references
    text = re.sub(r'\"[^"]*\.(graphql|react|rendererRef)[^\"]*\"', '', text)
    text = re.sub(r'\\"[^\\"]*\\.(graphql|react|rendererRef)[^\\"]*\\"', '', text)

    # Remove CSS, random commas, leftover brackets
    text = re.sub(r'css[\]\}\"]+', '', text)

    # Remove numbers
    text = re.sub(r'[0-9]+', '', text)

    # Collapse multiple spaces and newlines
    text = re.sub(r'\s+', ' ', text)

    # Remove non-ASCII characters
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)

    return text.strip()

def basic_text_preprocess(text):
    """
    Performs basic preprocessing such as lowering case, 
    removing punctuations for lighter tasks.

    Args:
        text (str): Input text.

    Returns:
        str: Preprocessed text.
    """
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()
