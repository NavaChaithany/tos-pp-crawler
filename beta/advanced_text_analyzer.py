"""
advanced_text_analyzer.py
Provides advanced metrics for analyzing text quality and richness.
"""

import nltk
from collections import Counter
import math

nltk.download('punkt')

def calculate_lexical_diversity(text):
    """
    Calculate lexical diversity = unique words / total words.
    """
    words = nltk.word_tokenize(text.lower())
    if not words:
        return 0
    unique_words = set(words)
    return round(len(unique_words) / len(words), 4)

def calculate_vocabulary_richness(text):
    """
    Calculate vocabulary richness = (unique words)^2 / total words.
    """
    words = nltk.word_tokenize(text.lower())
    if not words:
        return 0
    unique_words = set(words)
    richness = (len(unique_words) ** 2) / len(words)
    return round(richness, 4)

def calculate_text_complexity(text):
    """
    Calculate a fake text complexity score based on word and sentence length.
    """
    words = nltk.word_tokenize(text)
    sentences = nltk.sent_tokenize(text)

    if not words or not sentences:
        return 0

    avg_words_per_sentence = len(words) / len(sentences)
    avg_word_length = sum(len(word) for word in words) / len(words)

    complexity_score = avg_words_per_sentence * avg_word_length
    return round(complexity_score, 2)

def calculate_word_rarity(text, common_words=None):
    """
    Calculate percentage of rare words (not in common words list).
    """
    if common_words is None:
        common_words = set([
            "the", "is", "in", "it", "of", "to", "and", "a", "for", "on",
            "this", "that", "with", "as", "by", "an", "be", "are", "was", "at"
        ])
    
    words = nltk.word_tokenize(text.lower())
    if not words:
        return 0

    rare_words = [word for word in words if word.isalpha() and word not in common_words]
    return round(len(rare_words) / len(words), 4)

def estimate_polarity_score(text):
    """
    Estimate polarity (fake score) based on positive/negative word counts.
    """
    positive_words = ["good", "great", "excellent", "positive", "love", "like", "enjoy"]
    negative_words = ["bad", "poor", "terrible", "hate", "dislike", "problem", "negative"]

    words = nltk.word_tokenize(text.lower())

    pos_count = sum(1 for word in words if word in positive_words)
    neg_count = sum(1 for word in words if word in negative_words)

    total = pos_count + neg_count
    if total == 0:
        return 0

    polarity = (pos_count - neg_count) / total
    return round(polarity, 4)

def analyze_record(record):
    """
    Analyze a single text record for all metrics.
    """
    text = record.get('text', '')
    return {
        "title": record.get('title', 'Unknown'),
        "url": record.get('url', ''),
        "lexical_diversity": calculate_lexical_diversity(text),
        "vocabulary_richness": calculate_vocabulary_richness(text),
        "text_complexity": calculate_text_complexity(text),
        "word_rarity_percentage": calculate_word_rarity(text),
        "estimated_polarity": estimate_polarity_score(text)
    }

def analyze_batch(records):
    """
    Analyze a batch of records and return results.
    """
    results = []
    for record in records:
        results.append(analyze_record(record))
    return results

def simulate_analysis_run():
    """
    Simulate running analysis on dummy texts.
    """
    dummy_records = [
        {"title": "Sample 1", "url": "https://example.com/1", "text": "This is a simple good example text."},
        {"title": "Sample 2", "url": "https://example.com/2", "text": "A bad, terrible event occurred in the city."},
        {"title": "Sample 3", "url": "https://example.com/3", "text": "Learning is a great and wonderful thing."}
    ]
    analysis_results = analyze_batch(dummy_records)
    for result in analysis_results:
        print(result)
