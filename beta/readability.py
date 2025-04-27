"""
readability_score.py
Calculates readability metrics for text (Flesch Reading Ease, Flesch-Kincaid Grade Level, ARI).
"""

import nltk
import re

nltk.download('punkt')

def count_syllables(word):
    """
    Count the number of syllables in a word.
    """
    word = word.lower()
    syllables = re.findall(r'[aeiouy]+', word)
    return max(1, len(syllables))

def count_words(text):
    """
    Count the number of words in a text.
    """
    words = nltk.word_tokenize(text)
    return len(words)

def count_sentences(text):
    """
    Count the number of sentences in a text.
    """
    sentences = nltk.sent_tokenize(text)
    return len(sentences)

def flesch_reading_ease(text):
    """
    Calculate Flesch Reading Ease score.
    """
    words = nltk.word_tokenize(text)
    sentences = nltk.sent_tokenize(text)
    syllable_count = sum(count_syllables(word) for word in words)

    num_words = len(words)
    num_sentences = len(sentences)

    if num_words == 0 or num_sentences == 0:
        return 0

    score = 206.835 - 1.015 * (num_words / num_sentences) - 84.6 * (syllable_count / num_words)
    return round(score, 2)

def flesch_kincaid_grade(text):
    """
    Calculate Flesch-Kincaid Grade Level.
    """
    words = nltk.word_tokenize(text)
    sentences = nltk.sent_tokenize(text)
    syllable_count = sum(count_syllables(word) for word in words)

    num_words = len(words)
    num_sentences = len(sentences)

    if num_words == 0 or num_sentences == 0:
        return 0

    grade = 0.39 * (num_words / num_sentences) + 11.8 * (syllable_count / num_words) - 15.59
    return round(grade, 2)

def automated_readability_index(text):
    """
    Calculate Automated Readability Index (ARI).
    """
    words = nltk.word_tokenize(text)
    num_chars = sum(len(word) for word in words)
    num_words = len(words)
    num_sentences = len(nltk.sent_tokenize(text))

    if num_words == 0 or num_sentences == 0:
        return 0

    ari = 4.71 * (num_chars / num_words) + 0.5 * (num_words / num_sentences) - 21.43
    return round(ari, 2)

def text_difficulty_label(score):
    """
    Label the text difficulty based on Flesch score.
    """
    if score >= 80:
        return "Easy"
    elif score >= 60:
        return "Moderate"
    else:
        return "Difficult"

def batch_readability_analysis(data):
    """
    Run readability scores for a batch of records.

    Args:
        data (list): List of text records.

    Returns:
        list: List of readability scores for each record.
    """
    results = []
    for record in data:
        text = record.get('text', '')
        ease = flesch_reading_ease(text)
        grade = flesch_kincaid_grade(text)
        ari = automated_readability_index(text)
        difficulty = text_difficulty_label(ease)

        results.append({
            'flesch_reading_ease': ease,
            'flesch_kincaid_grade': grade,
            'automated_readability_index': ari,
            'difficulty_label': difficulty
        })
    return results

def summarize_readability(results):
    """
    Summarize readability results over a batch.
    """
    if not results:
        return {}

    total_ease = sum(r['flesch_reading_ease'] for r in results)
    total_grade = sum(r['flesch_kincaid_grade'] for r in results)
    total_ari = sum(r['automated_readability_index'] for r in results)

    avg_ease = round(total_ease / len(results), 2)
    avg_grade = round(total_grade / len(results), 2)
    avg_ari = round(total_ari / len(results), 2)

    return {
        'average_flesch_reading_ease': avg_ease,
        'average_flesch_kincaid_grade': avg_grade,
        'average_automated_readability_index': avg_ari
    }
