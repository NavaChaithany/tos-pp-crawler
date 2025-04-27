"""
text_similarity_engine.py
Provides utilities for measuring text similarity and detecting duplicates.
"""

import math
import re
from collections import Counter

def tokenize(text):
    """
    Basic text tokenizer: lowercase and split by non-word characters.
    """
    tokens = re.findall(r'\b\w+\b', text.lower())
    return tokens

def text_to_vector(text):
    """
    Convert text to a vector of word counts.
    """
    words = tokenize(text)
    return Counter(words)

def cosine_similarity(vec1, vec2):
    """
    Calculate cosine similarity between two vectors.
    """
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([v ** 2 for v in vec1.values()])
    sum2 = sum([v ** 2 for v in vec2.values()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

def compute_similarity(text1, text2):
    """
    Compute cosine similarity between two texts.
    """
    vector1 = text_to_vector(text1)
    vector2 = text_to_vector(text2)
    similarity = cosine_similarity(vector1, vector2)
    return similarity

def find_near_duplicates(records, threshold=0.85):
    """
    Find near-duplicate records based on text similarity.
    """
    duplicates = []
    for i in range(len(records)):
        for j in range(i + 1, len(records)):
            sim = compute_similarity(records[i].get('text', ''),
                                     records[j].get('text', ''))
            if sim >= threshold:
                duplicates.append({
                    'record1': records[i].get('title', f'Record {i}'),
                    'record2': records[j].get('title', f'Record {j}'),
                    'similarity': sim
                })
    return duplicates

def save_duplicate_report(duplicates, filename='duplicate_report.txt'):
    """
    Save near-duplicate findings to a report file.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        for dup in duplicates:
            f.write(f"{dup['record1']} <--> {dup['record2']} | Similarity: {dup['similarity']:.2f}\n")
    print(f"Duplicate report saved to {filename}")

def simulate_similarity_check():
    """
    Simulate running similarity detection on dummy data.
    """
    dummy_records = [
        {"title": "Doc A", "text": "The quick brown fox jumps over the lazy dog."},
        {"title": "Doc B", "text": "A quick brown fox jumped over a very lazy dog!"},
        {"title": "Doc C", "text": "An entirely different sentence without relation."}
    ]

    print("\nFinding Near-Duplicates...")
    duplicates = find_near_duplicates(dummy_records, threshold=0.7)

    for dup in duplicates:
        print(f"Duplicate: {dup['record1']} <--> {dup['record2']} | Similarity: {dup['similarity']:.2f}")

    save_duplicate_report(duplicates)

