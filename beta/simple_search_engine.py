"""
simple_search_engine.py
Provides basic keyword search functionality over a batch of crawled records.
"""

import nltk

nltk.download('punkt')

def keyword_in_text(text, keyword):
    """
    Check if keyword exists in text.

    Args:
        text (str): Text to search.
        keyword (str): Keyword to find.

    Returns:
        bool: True if found, False otherwise.
    """
    return keyword.lower() in text.lower()

def search_record(record, keyword):
    """
    Search for a keyword in a single record.

    Args:
        record (dict): A dictionary with a 'text' field.
        keyword (str): Keyword to find.

    Returns:
        bool: True if keyword found, False otherwise.
    """
    return keyword_in_text(record.get('text', ''), keyword)

def search_batch(records, keyword):
    """
    Search for a keyword across multiple records.

    Args:
        records (list): List of record dictionaries.
        keyword (str): Keyword to search for.

    Returns:
        list: List of matching records.
    """
    matching_records = []
    for record in records:
        if search_record(record, keyword):
            matching_records.append(record)
    return matching_records

def count_keyword_occurrences(text, keyword):
    """
    Count the number of times a keyword appears in text.

    Args:
        text (str): Text to search.
        keyword (str): Keyword to count.

    Returns:
        int: Number of occurrences.
    """
    words = nltk.word_tokenize(text.lower())
    return words.count(keyword.lower())

def batch_keyword_statistics(records, keyword):
    """
    Calculate total keyword occurrences across all records.

    Args:
        records (list): List of record dictionaries.
        keyword (str): Keyword to search.

    Returns:
        dict: Statistics about keyword occurrences.
    """
    total_occurrences = 0
    records_with_keyword = 0

    for record in records:
        count = count_keyword_occurrences(record.get('text', ''), keyword)
        if count > 0:
            records_with_keyword += 1
            total_occurrences += count

    avg_occurrences_per_record = (total_occurrences / records_with_keyword) if records_with_keyword else 0

    return {
        "total_records": len(records),
        "records_with_keyword": records_with_keyword,
        "total_occurrences": total_occurrences,
        "average_occurrences_per_matching_record": round(avg_occurrences_per_record, 2)
    }

def multiple_keywords_search(records, keywords):
    """
    Search for multiple keywords in a batch.

    Args:
        records (list): List of records.
        keywords (list): List of keywords.

    Returns:
        dict: Mapping keyword to matching records.
    """
    keyword_results = {}

    for keyword in keywords:
        matches = search_batch(records, keyword)
        keyword_results[keyword] = {
            "match_count": len(matches),
            "matched_titles": [record.get('title', '') for record in matches]
        }

    return keyword_results

def example_search_run(records):
    """
    Example usage of the simple search engine.
    """
    print("Running search example...")
    keywords = ["privacy", "terms", "data"]

    for keyword in keywords:
        print(f"\nSearching for '{keyword}'...")
        stats = batch_keyword_statistics(records, keyword)
        print(stats)

    print("\nRunning multi-keyword search...")
    multi_stats = multiple_keywords_search(records, keywords)
    print(multi_stats)
