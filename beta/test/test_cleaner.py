"""
tests/test_cleaner.py
Unit tests for text_cleaner.py functions.
"""

import unittest
from text_cleaner import clean_text, basic_text_preprocess

class TestTextCleaner(unittest.TestCase):

    def test_clean_text_basic_removal(self):
        dirty_text = "window.test = 'value'; Some normal text. function() { return 1; }"
        cleaned = clean_text(dirty_text)
        self.assertNotIn("window", cleaned)
        self.assertNotIn("function", cleaned)
        self.assertIn("Some normal text.", cleaned)

    def test_clean_text_braces_removal(self):
        dirty_text = "Hello {garbage} World."
        cleaned = clean_text(dirty_text)
        self.assertNotIn("{", cleaned)
        self.assertNotIn("}", cleaned)
        self.assertIn("Hello", cleaned)

    def test_basic_text_preprocess_lowercase(self):
        raw_text = "Hello World!"
        processed = basic_text_preprocess(raw_text)
        self.assertEqual(processed, "hello world")

    def test_basic_text_preprocess_removal(self):
        raw_text = "Hi! How are you? 1234!!"
        processed = basic_text_preprocess(raw_text)
        self.assertEqual(processed, "hi how are you")

if __name__ == "__main__":
    unittest.main()
