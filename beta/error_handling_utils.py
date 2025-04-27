"""
error_handling_utils.py
Provides utilities for error handling, retry logic, and error logging.
"""

import time
import random

class CrawlerTimeoutError(Exception):
    """Custom exception for crawler timeout errors."""
    pass

class CrawlerConnectionError(Exception):
    """Custom exception for crawler connection failures."""
    pass

def retry_on_failure(retries=3, delay=1):
    """
    Decorator to retry a function if it fails.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed: {str(e)}")
                    time.sleep(delay)
                    attempt += 1
            raise Exception(f"All {retries} attempts failed.")
        return wrapper
    return decorator

@retry_on_failure(retries=3, delay=2)
def unstable_operation():
    """
    Simulate an unstable operation that randomly fails.
    """
    if random.random() < 0.7:
        raise CrawlerConnectionError("Simulated random connection failure.")
    return "Operation Successful!"

def simulate_timeout_operation():
    """
    Simulate an operation that sometimes times out.
    """
    time.sleep(random.uniform(0.5, 1.5))
    if random.random() < 0.3:
        raise CrawlerTimeoutError("Simulated operation timeout.")

def safe_execute(func, *args, **kwargs):
    """
    Safely execute a function and handle exceptions.
    """
    try:
        result = func(*args, **kwargs)
        return {"status": "success", "result": result}
    except Exception as e:
        log_error(str(e))
        return {"status": "failure", "error": str(e)}

def log_error(message, logfile='errors.log'):
    """
    Log an error message to a logfile.
    """
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open(logfile, 'a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] ERROR: {message}\n")
    print(f"Logged error: {message}")

def simulate_error_handling_flow():
    """
    Simulate a full error-handling workflow.
    """
    print("\nSimulating unstable operation with retries:")
    try:
        result = unstable_operation()
        print(f"Result: {result}")
    except Exception as e:
        print(f"Final failure: {e}")

    print("\nSimulating timeout-prone operation:")
    outcome = safe_execute(simulate_timeout_operation)
    print(f"Outcome: {outcome}")

    print("\nChecking logged errors...")
    try:
        with open('errors.log', 'r', encoding='utf-8') as f:
            logs = f.readlines()
            print(f"Found {len(logs)} log entries.")
    except FileNotFoundError:
        print("No logs found.")

