"""
text_summarizer_utils.py
Provides text summarization utilities for batch records.
"""

import nltk

nltk.download('punkt')

def generate_100_word_summary(text):
    """
    Generate a 100-word summary from the given text.
    """
    words = nltk.word_tokenize(text)
    if len(words) <= 100:
        return text
    return ' '.join(words[:100])

def generate_one_sentence_summary(text):
    """
    Generate a one-sentence summary (longest sentence).
    """
    sentences = nltk.sent_tokenize(text)
    if not sentences:
        return ""
    longest_sentence = max(sentences, key=len)
    return longest_sentence

def summarize_record(record):
    """
    Summarize a single record with both types of summaries.
    """
    text = record.get('text', '')
    return {
        "title": record.get('title', 'Unknown'),
        "url": record.get('url', ''),
        "summary_100_words": generate_100_word_summary(text),
        "summary_one_sentence": generate_one_sentence_summary(text)
    }

def summarize_batch(records):
    """
    Summarize a batch of text records.
    """
    summaries = []
    for record in records:
        summary = summarize_record(record)
        summaries.append(summary)
    return summaries

def simulate_summarization_run():
    """
    Simulate summarizing dummy records.
    """
    dummy_records = [
        {"title": "Doc A", "url": "https://example.com/a", "text": "This is a very simple document. It has only a few words."},
        {"title": "Doc B", "url": "https://example.com/b", "text": " ".join(["word"] * 150)}
    ]

    summaries = summarize_batch(dummy_records)
    for summary in summaries:
        print("\nSummary for:", summary['title'])
        print("100-word Summary:", summary['summary_100_words'])
        print("One-sentence Summary:", summary['summary_one_sentence'])

