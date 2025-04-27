"""
crawler_scheduler.py
Manages scheduling of crawl tasks, retries, and crawler states.
"""

import time
import random
from queue import PriorityQueue

class CrawlTask:
    """
    Represents a single crawl task.
    """
    def __init__(self, url, priority=5):
        self.url = url
        self.priority = priority
        self.timestamp = time.time()

    def __lt__(self, other):
        return self.priority < other.priority

class CrawlerScheduler:
    """
    Schedules and manages crawl tasks.
    """

    def __init__(self):
        self.task_queue = PriorityQueue()
        self.paused = False

    def add_task(self, url, priority=5):
        """
        Add a new crawl task to the queue.
        """
        task = CrawlTask(url, priority)
        self.task_queue.put(task)
        print(f"Added task: {url} with priority {priority}")

    def get_next_task(self):
        """
        Fetch the next task based on priority.
        """
        if self.paused:
            print("Crawler is paused. No task fetched.")
            return None
        if self.task_queue.empty():
            print("No tasks in the queue.")
            return None
        task = self.task_queue.get()
        print(f"Fetching task: {task.url}")
        return task

    def simulate_crawling_task(self, task):
        """
        Simulate executing a crawl task.
        """
        print(f"Crawling URL: {task.url}...")
        time.sleep(random.uniform(0.1, 0.3))  # Simulated work
        if random.random() < 0.1:
            print(f"Failed to crawl {task.url}. Re-adding with lower priority.")
            self.add_task(task.url, priority=task.priority + 1)
        else:
            print(f"Successfully crawled {task.url}.")

    def run_scheduler_loop(self, max_tasks=10):
        """
        Run the crawler scheduler.
        """
        tasks_executed = 0
        while not self.task_queue.empty() and tasks_executed < max_tasks:
            if self.paused:
                print("Scheduler is paused. Waiting...")
                time.sleep(1)
                continue
            task = self.get_next_task()
            if task:
                self.simulate_crawling_task(task)
                tasks_executed += 1
            else:
                break

    def pause(self):
        """
        Pause the scheduler.
        """
        self.paused = True
        print("Scheduler paused.")

    def resume(self):
        """
        Resume the scheduler.
        """
        self.paused = False
        print("Scheduler resumed.")

def simulate_scheduler_run():
    """
    Simulate a full scheduler run.
    """
    scheduler = CrawlerScheduler()
    urls = [f"https://example.com/page/{i}" for i in range(15)]

    print("\nAdding tasks to scheduler...")
    for url in urls:
        priority = random.randint(1, 10)
        scheduler.add_task(url, priority=priority)

    print("\nRunning scheduler...")
    scheduler.run_scheduler_loop(max_tasks=12)

    print("\nPausing crawler...")
    scheduler.pause()

    time.sleep(2)

    print("\nResuming crawler...")
    scheduler.resume()
    scheduler.run_scheduler_loop(max_tasks=5)

