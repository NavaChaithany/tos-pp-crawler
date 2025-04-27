"""
crawler_simulation_tools.py
Simulates a basic crawler engine with random delays, successes, and failures.
"""

import random
import time

def simulate_page_fetch(url):
    """
    Simulate fetching a page with random success/failure.
    """
    print(f"Fetching URL: {url}")
    time.sleep(random.uniform(0.1, 0.3))  # Simulated network delay

    if random.random() < 0.85:
        return {"status": "success", "content": f"Simulated content from {url}"}
    else:
        return {"status": "failure", "error": "Fetch failed"}

def simulate_crawl_batch(urls):
    """
    Simulate crawling a batch of URLs.
    """
    crawled_data = []
    for url in urls:
        result = simulate_page_fetch(url)
        crawled_data.append({
            "url": url,
            "result": result
        })
    return crawled_data

def retry_failed_fetches(crawled_batch, max_retries=2):
    """
    Retry failed fetches up to max_retries.
    """
    retried_data = []
    for entry in crawled_batch:
        url = entry['url']
        result = entry['result']
        retries = 0

        while result.get('status') != 'success' and retries < max_retries:
            print(f"Retrying URL: {url} (Attempt {retries + 1})")
            result = simulate_page_fetch(url)
            retries += 1

        retried_data.append({
            "url": url,
            "result": result
        })
    return retried_data

def simulate_large_scale_crawl(url_base, count=100):
    """
    Simulate a large number of URL crawls.
    """
    urls = [f"{url_base}/page/{i}" for i in range(count)]
    print(f"Starting large-scale crawl of {count} URLs...")
    crawled_data = simulate_crawl_batch(urls)
    retried_data = retry_failed_fetches(crawled_data)
    return retried_data

def collect_successful_data(crawled_batch):
    """
    Collect successful crawl contents only.
    """
    successful_data = []
    for entry in crawled_batch:
        if entry['result'].get('status') == 'success':
            successful_data.append(entry['result']['content'])
    return successful_data

def log_crawl_errors(crawled_batch):
    """
    Log errors from crawl failures.
    """
    for entry in crawled_batch:
        if entry['result'].get('status') != 'success':
            print(f"Error fetching {entry['url']}: {entry['result'].get('error')}")

def simulate_full_crawl_process():
    """
    Simulate full crawler process with retry and collection.
    """
    url_base = "https://examplecrawler.com"
    crawled_data = simulate_large_scale_crawl(url_base, count=20)

    print("\nCollecting Successful Data...")
    successful_data = collect_successful_data(crawled_data)
    print(f"Total successful pages: {len(successful_data)}")

    print("\nLogging Crawl Errors...")
    log_crawl_errors(crawled_data)

    print("\nCrawl Simulation Complete.")

