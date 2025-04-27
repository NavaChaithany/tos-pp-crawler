"""
crawler_statistics_collector.py
Collects runtime statistics during crawling operations.
"""

import time
import random
import json
import os

class CrawlerStatistics:
    """
    Collect and report crawler runtime statistics.
    """

    def __init__(self):
        self.start_time = time.time()
        self.urls_crawled = 0
        self.errors_encountered = 0
        self.total_crawl_time = 0.0
        self.crawl_records = []

    def record_crawl(self, url, success=True, crawl_time=0.0):
        """
        Record the result of a crawl attempt.
        """
        self.urls_crawled += 1
        if not success:
            self.errors_encountered += 1
        self.total_crawl_time += crawl_time
        self.crawl_records.append({
            "url": url,
            "success": success,
            "crawl_time_sec": crawl_time
        })

    def average_crawl_time(self):
        """
        Compute average time per crawl.
        """
        if self.urls_crawled == 0:
            return 0.0
        return self.total_crawl_time / self.urls_crawled

    def total_runtime(self):
        """
        Total runtime since crawler started.
        """
        return time.time() - self.start_time

    def generate_summary(self):
        """
        Generate a crawler statistics summary.
        """
        summary = {
            "total_urls_crawled": self.urls_crawled,
            "errors_encountered": self.errors_encountered,
            "average_crawl_time_sec": round(self.average_crawl_time(), 3),
            "total_runtime_sec": round(self.total_runtime(), 2)
        }
        return summary

    def save_summary(self, filename="crawler_summary.json"):
        """
        Save the summary report to a JSON file.
        """
        summary = self.generate_summary()
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=4)
        print(f"Summary saved to {filename}")

def simulate_crawler_run():
    """
    Simulate a crawler run collecting stats.
    """
    stats = CrawlerStatistics()

    urls = [f"https://example.com/page/{i}" for i in range(10)]

    for url in urls:
        crawl_time = random.uniform(0.1, 0.5)
        success = random.choice([True, True, True, False])  # 75% chance success
        time.sleep(crawl_time)
        stats.record_crawl(url, success=success, crawl_time=crawl_time)
        print(f"Crawled {url} | Success: {success} | Time: {crawl_time:.2f}s")

    print("\nFinal Crawler Summary:")
    summary = stats.generate_summary()
    for k, v in summary.items():
        print(f"{k}: {v}")

    stats.save_summary()

