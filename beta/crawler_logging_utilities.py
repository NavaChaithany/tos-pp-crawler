"""
crawler_logging_utilities.py
Provides utilities for logging crawler activities.
"""

import os
from datetime import datetime

class CrawlerLogger:
    """
    Logger for crawler events.
    """

    def __init__(self, log_folder='logs'):
        self.log_folder = log_folder
        if not os.path.exists(self.log_folder):
            os.makedirs(self.log_folder)
        self.log_file = os.path.join(self.log_folder, f"crawler_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")

    def log_event(self, message):
        """
        Log a general event.
        """
        with open(self.log_file, 'a', encoding='utf-8') as f:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            f.write(f"[INFO] {timestamp} - {message}\n")

    def log_error(self, error_message):
        """
        Log an error event.
        """
        with open(self.log_file, 'a', encoding='utf-8') as f:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            f.write(f"[ERROR] {timestamp} - {error_message}\n")

    def log_success(self, url):
        """
        Log a successful crawl.
        """
        with open(self.log_file, 'a', encoding='utf-8') as f:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            f.write(f"[SUCCESS] {timestamp} - Successfully crawled {url}\n")

def simulate_logging_example():
    """
    Simulate using the logger.
    """
    logger = CrawlerLogger()

    logger.log_event("Crawler started")
    logger.log_success("https://example.com/page1")
    logger.log_success("https://example.com/page2")
    logger.log_error("Failed to crawl https://example.com/page3 due to timeout")
    logger.log_event("Crawler finished successfully")

