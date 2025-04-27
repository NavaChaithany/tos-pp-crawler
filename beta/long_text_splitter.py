"""
long_text_splitter.py
Splits very long texts into paragraphs or smaller chunks for easier processing.
"""

import nltk

nltk.download('punkt')

def split_into_sentences(text):
    """
    Split text into a list of sentences.

    Args:
        text (str): Input text.

    Returns:
        list: List of sentences.
    """
    sentences = nltk.sent_tokenize(text)
    return sentences

def split_by_fixed_sentence_count(text, sentence_per_chunk=5):
    """
    Split text into chunks, each with a fixed number of sentences.

    Args:
        text (str): Input text.
        sentence_per_chunk (int): Number of sentences per chunk.

    Returns:
        list: List of text chunks.
    """
    sentences = split_into_sentences(text)
    chunks = []
    for i in range(0, len(sentences), sentence_per_chunk):
        chunk = ' '.join(sentences[i:i+sentence_per_chunk])
        chunks.append(chunk)
    return chunks

def split_by_word_limit(text, word_limit=100):
    """
    Split text into chunks of approximate word limits.

    Args:
        text (str): Input text.
        word_limit (int): Max number of words per chunk.

    Returns:
        list: List of text chunks.
    """
    words = nltk.word_tokenize(text)
    chunks = []
    for i in range(0, len(words), word_limit):
        chunk = ' '.join(words[i:i+word_limit])
        chunks.append(chunk)
    return chunks

def count_chunks_by_sentences(text, sentence_per_chunk=5):
    """
    Return how many chunks would be formed based on sentences.

    Args:
        text (str): Input text.

    Returns:
        int: Number of chunks.
    """
    return len(split_by_fixed_sentence_count(text, sentence_per_chunk))

def count_chunks_by_words(text, word_limit=100):
    """
    Return how many chunks would be formed based on words.

    Args:
        text (str): Input text.

    Returns:
        int: Number of chunks.
    """
    return len(split_by_word_limit(text, word_limit))

def example_usage(text):
    """
    Example usage of long_text_splitter functions.
    """
    print(f"Original text length: {len(text)} characters")
    print(f"Splitting into sentence chunks...")
    chunks = split_by_fixed_sentence_count(text)
    print(f"Generated {len(chunks)} sentence-based chunks.")
    print(f"Splitting into word chunks...")
    word_chunks = split_by_word_limit(text)
    print(f"Generated {len(word_chunks)} word-based chunks.")
