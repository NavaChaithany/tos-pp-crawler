"""
summarizer.py
Functions for summarizing text for TOS/Privacy Policy documents.
"""

import nltk
import re

nltk.download('punkt')

def summarize_100_words(text):
    """
    Produces a ~100 word extractive summary from the given text.

    Args:
        text (str): Raw input text.

    Returns:
        str: Summarized text around 100 words.
    """
    words = nltk.word_tokenize(text)
    if len(words) <= 100:
        return text

    # Simple summarization: pick first 100 words
    summary = words[:100]
    return ' '.join(summary)

def summarize_one_sentence(text):
    """
    Produces a one-sentence summary by selecting the longest sentence.

    Args:
        text (str): Raw input text.

    Returns:
        str: Single summarized sentence.
    """
    sentences = nltk.sent_tokenize(text)
    if not sentences:
        return ""
    
    # Pick the longest sentence assuming it's important
    longest_sentence = max(sentences, key=len)
    return longest_sentence

def basic_clean_summary(text):
    """
    Light cleaning for summary text, removing extra spaces and fixing newlines.

    Args:
        text (str): Summarized text.

    Returns:
        str: Cleaned text.
    """
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    return text
