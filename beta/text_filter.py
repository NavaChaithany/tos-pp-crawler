"""
text_filter.py
Advanced text cleaning functions for TOS/Privacy Policy datasets.
"""

import re
import html

def remove_html_tags(text):
    """
    Remove HTML tags like <div>, <p>, <span>, etc.

    Args:
        text (str): Raw input text.

    Returns:
        str: Text without HTML tags.
    """
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def remove_special_unicode(text):
    """
    Remove special unicode characters (emojis, non-ASCII).

    Args:
        text (str): Raw input text.

    Returns:
        str: ASCII-only cleaned text.
    """
    return text.encode('ascii', 'ignore').decode('ascii')

def remove_javascript_snippets(text):
    """
    Remove JavaScript-like blocks inside <script> tags.

    Args:
        text (str): Raw input text.

    Returns:
        str: Text with JavaScript snippets removed.
    """
    pattern = re.compile(r'<script.*?>.*?</script>', re.DOTALL)
    return re.sub(pattern, '', text)

def remove_css_styles(text):
    """
    Remove CSS-like blocks inside <style> tags.

    Args:
        text (str): Raw input text.

    Returns:
        str: Text with CSS styles removed.
    """
    pattern = re.compile(r'<style.*?>.*?</style>', re.DOTALL)
    return re.sub(pattern, '', text)

def html_unescape(text):
    """
    Decode HTML entities like &amp;, &lt;, etc. into normal characters.

    Args:
        text (str): Text with HTML entities.

    Returns:
        str: Clean text.
    """
    return html.unescape(text)

def advanced_clean(text):
    """
    Apply all advanced cleaning steps.

    Args:
        text (str): Raw text.

    Returns:
        str: Fully cleaned text.
    """
    text = remove_html_tags(text)
    text = remove_special_unicode(text)
    text = remove_javascript_snippets(text)
    text = remove_css_styles(text)
    text = html_unescape(text)
    text = text.strip()
    return text
