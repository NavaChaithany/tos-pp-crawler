'''
entity_counter.py
Extracts and counts named entities (ORG, PERSON, GPE) from text.
"""

import nltk
from collections import Counter

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

def extract_named_entities(text):
    """
    Extract named entities from text using NLTK.

    Args:
        text (str): Input text.

    Returns:
        list: List of named entities.
    """
    words = nltk.word_tokenize(text)
    pos_tags = nltk.pos_tag(words)
    chunked = nltk.ne_chunk(pos_tags)

    entities = []
    for chunk in chunked:
        if hasattr(chunk, 'label'):
            entity_name = ' '.join(c[0] for c in chunk)
            entity_type = chunk.label()
            entities.append((entity_name, entity_type))
    return entities

def count_entity_types(entities):
    """
    Count occurrences of each entity type.

    Args:
        entities (list): List of (entity_name, entity_type) tuples.

    Returns:
        dict: Mapping of entity type to count.
    """
    counter = Counter([etype for _, etype in entities])
    return dict(counter)

def extract_and_count(text):
    """
    High-level function: extract entities and count them.

    Args:
        text (str): Input text.

    Returns:
        dict: Dictionary with counts per entity type.
    """
    entities = extract_named_entities(text)
    counts = count_entity_types(entities)
    return counts
