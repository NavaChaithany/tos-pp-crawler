"""
tests/test_miner.py
Unit tests for text_miner.py functions.
"""

import unittest
from text_miner import (
    basic_text_statistics,
    most_frequent_noun,
    most_frequent_verb,
    sentiment_score,
    named_entities
)

class TestTextMiner(unittest.TestCase):

    def test_basic_text_statistics(self):
        text = "Hello world. This is a test sentence."
        stats = basic_text_statistics(text)
        self.assertEqual(stats['total_sentences'], 2)
        self.assertGreater(stats['total_words'], 5)
        self.assertGreater(stats['avg_words_per_sentence'], 2)

    def test_most_frequent_noun(self):
        text = "Dog runs faster than another dog."
        noun = most_frequent_noun(text)
        self.assertEqual(noun.lower(), "dog")

    def test_most_frequent_verb(self):
        text = "Run and jump and run again."
        verb = most_frequent_verb(text)
        self.assertIn(verb.lower(), ["run", "jump"])

    def test_sentiment_score_positive(self):
        text = "I love this awesome project!"
        score = sentiment_score(text)
        self.assertGreater(score, 0)

    def test_sentiment_score_negative(self):
        text = "I hate this terrible experience."
        score = sentiment_score(text)
        self.assertLess(score, 0)

    def test_named_entities_extraction(self):
        text = "Barack Obama was the President of United States."
        entities = named_entities(text)
        entity_names = [entity for entity, label in entities]
        self.assertIn("Barack Obama", entity_names)

if __name__ == "__main__":
    unittest.main()
