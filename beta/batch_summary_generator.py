"""
batch_summary_generator.py
Generates summaries (100-word, 1-sentence, word frequency stats) for batches of records.
"""

import nltk
from collections import Counter

nltk.download('punkt')

def generate_100_word_summary(text):
    """
    Generate a 100-word summary from the text.
    """
    words = nltk.word_tokenize(text)
    summary = ' '.join(words[:100])
    return summary

def generate_one_sentence_summary(text):
    """
    Generate a one-sentence summary from the text.
    """
    sentences = nltk.sent_tokenize(text)
    if sentences:
        return sentences[0]
    return ""

def calculate_word_frequencies(text):
    """
    Calculate word frequencies in the text.
    """
    words = nltk.word_tokenize(text.lower())
    words = [word for word in words if word.isalpha()]
    counter = Counter(words)
    return dict(counter.most_common(10))

def summarize_record(record):
    """
    Summarize a single record.

    Args:
        record (dict): Dictionary with 'text' key.

    Returns:
        dict: Summary stats for one record.
    """
    text = record.get('text', '')
    return {
        "title": record.get('title', 'Unknown'),
        "url": record.get('url', ''),
        "100_word_summary": generate_100_word_summary(text),
        "one_sentence_summary": generate_one_sentence_summary(text),
        "top_10_words": calculate_word_frequencies(text)
    }

def summarize_batch(records):
    """
    Summarize an entire batch of records.

    Args:
        records (list): List of record dictionaries.

    Returns:
        list: List of summarized records.
    """
    summaries = []
    for record in records:
        summaries.append(summarize_record(record))
    return summaries

def summarize_word_counts(records):
    """
    Get average word counts across all records.
    """
    total_words = 0
    total_sentences = 0
    for record in records:
        text = record.get('text', '')
        total_words += len(nltk.word_tokenize(text))
        total_sentences += len(nltk.sent_tokenize(text))
    avg_words = total_words / len(records) if records else 0
    avg_sentences = total_sentences / len(records) if records else 0
    return {
        "average_words_per_record": round(avg_words, 2),
        "average_sentences_per_record": round(avg_sentences, 2)
    }

def batch_top_words(records, top_n=20):
    """
    Get most frequent words across entire batch.

    Args:
        records (list): List of record dicts.
        top_n (int): Number of top words to return.

    Returns:
        dict: Word frequency counts.
    """
    total_words = []
    for record in records:
        words = nltk.word_tokenize(record.get('text', '').lower())
        words = [word for word in words if word.isalpha()]
        total_words.extend(words)

    counter = Counter(total_words)
    return dict(counter.most_common(top_n))

def example_batch_run(records):
    """
    Example function to show batch summarization.
    """
    print("Generating batch summaries...")
    summaries = summarize_batch(records)
    print(f"Total summaries generated: {len(summaries)}")

    print("Calculating average stats...")
    stats = summarize_word_counts(records)
    print(stats)

    print("Extracting top words from batch...")
    top_words = batch_top_words(records)
    print(top_words)
