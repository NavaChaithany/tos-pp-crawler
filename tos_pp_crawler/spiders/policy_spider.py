import scrapy
from tos_pp_crawler.text_utils import get_sentiment

class PolicySpider(scrapy.Spider):
    name = "policy_spider"
    start_urls = [
        "https://www.apple.com/legal/privacy/",
        "https://policies.google.com/privacy",
        "https://privacy.microsoft.com/"
    ]

    def parse(self, response):
        # Extract all text from the page
        full_text = " ".join(response.css("body::text").getall()).strip()
        
        # Calculate text statistics and sentiment
        sentiment = get_sentiment(full_text)
        
        yield {
            'url': response.url,
            'text': full_text[:500],  # First 500 characters
            'word_count': len(full_text.split()),
            'char_count': len(full_text),
            'polarity': sentiment['polarity'],  # Sentiment between -1 (negative) and 1 (positive)
            'subjectivity': sentiment['subjectivity']  # 0 (objective) to 1 (subjective)
        }