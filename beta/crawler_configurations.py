"""
crawler_configurations.py
Defines configuration settings and utilities for the crawler system.
"""

class CrawlerConfig:
    """
    Stores crawler runtime configuration.
    """

    def __init__(self):
        self.max_retries = 3
        self.timeout_seconds = 10
        self.user_agent = "TOS-PP-Crawler/1.0"
        self.batch_size = 10
        self.allow_redirects = True
        self.headers = {
            "User-Agent": self.user_agent
        }
    
    def update_max_retries(self, retries):
        """
        Update maximum retry attempts.
        """
        if retries >= 0:
            self.max_retries = retries

    def update_timeout(self, timeout_sec):
        """
        Update timeout for requests.
        """
        if timeout_sec > 0:
            self.timeout_seconds = timeout_sec

    def update_batch_size(self, batch_size):
        """
        Update number of URLs per batch crawl.
        """
        if batch_size > 0:
            self.batch_size = batch_size

    def set_custom_user_agent(self, agent_string):
        """
        Set a custom User-Agent string.
        """
        if agent_string:
            self.user_agent = agent_string
            self.headers["User-Agent"] = agent_string

    def display_config(self):
        """
        Print current crawler configuration.
        """
        print("\nCurrent Crawler Configuration:")
        print(f"Max Retries: {self.max_retries}")
        print(f"Timeout (seconds): {self.timeout_seconds}")
        print(f"User-Agent: {self.user_agent}")
        print(f"Batch Size: {self.batch_size}")
        print(f"Allow Redirects: {self.allow_redirects}")

def simulate_config_usage():
    """
    Simulate updating and viewing crawler config.
    """
    config = CrawlerConfig()
    config.display_config()

    print("\nUpdating config dynamically...")
    config.update_max_retries(5)
    config.update_timeout(15)
    config.update_batch_size(25)
    config.set_custom_user_agent("CustomBot/2.0")

    config.display_config()

