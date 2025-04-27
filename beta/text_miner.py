"""
text_miner.py
Functions for basic text mining and analysis.
"""

import nltk
import re
from collections import Counter

# Ensure required NLTK data packages are downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('vader_lexicon')
nltk.download('maxent_ne_chunker')
nltk.download('words')

from nltk.sentiment import SentimentIntensityAnalyzer
from nltk import word_tokenize, sent_tokenize, pos_tag, ne_chunk

# Initialize Sentiment Analyzer once
sia = SentimentIntensityAnalyzer()

def basic_text_statistics(text):
    """
    Calculates basic text statistics.

    Args:
        text (str): Input text.

    Returns:
        dict: Dictionary with total words, total sentences, and average words per sentence.
    """
    words = word_tokenize(text)
    sentences = sent_tokenize(text)

    total_words = len(words)
    total_sentences = len(sentences)
    avg_words_per_sentence = total_words / total_sentences if total_sentences > 0 else 0

    return {
        "total_words": total_words,
        "total_sentences": total_sentences,
        "avg_words_per_sentence": avg_words_per_sentence
    }

def most_frequent_noun(text):
    """
    Finds the most frequent noun in the text.

    Args:
        text (str): Input text.

    Returns:
        str: Most common noun or None.
    """
    words = word_tokenize(text)
    pos_tags = pos_tag(words)
    nouns = [word for word, pos in pos_tags if pos.startswith('NN')]

    if nouns:
        most_common_noun = Counter(nouns).most_common(1)[0][0]
    else:
        most_common_noun = None

    return most_common_noun

def most_frequent_verb(text):
    """
    Finds the most frequent verb in the text.

    Args:
        text (str): Input text.

    Returns:
        str: Most common verb or None.
    """
    words = word_tokenize(text)
    pos_tags = pos_tag(words)
    verbs = [word for word, pos in pos_tags if pos.startswith('VB')]

    if verbs:
        most_common_verb = Counter(verbs).most_common(1)[0][0]
    else:
        most_common_verb = None

    return most_common_verb

def sentiment_score(text):
    """
    Calculates sentiment polarity score.

    Args:
        text (str): Input text.

    Returns:
        float: Compound sentiment score.
    """
    sentiment = sia.polarity_scores(text)
    return sentiment['compound']

def named_entities(text):
    """
    Extracts named entities from the text.

    Args:
        text (str): Input text.

    Returns:
        list: List of named entity tuples (entity, label).
    """
    words = word_tokenize(text)
    pos_tags = pos_tag(words)
    tree = ne_chunk(pos_tags, binary=False)

    entities = []
    for subtree in tree.subtrees():
        if subtree.label() != 'S':
            entity = " ".join(word for word, tag in subtree.leaves())
            entities.append((entity, subtree.label()))
    return entities
