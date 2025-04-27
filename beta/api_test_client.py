"""
api_test_client.py
Simulates API requests and responses for testing the crawler system.
"""

import random
import time

def simulate_get_request(url):
    """
    Simulate a GET request to a URL.
    """
    print(f"Sending GET request to {url}")
    time.sleep(random.uniform(0.1, 0.5))
    if random.random() < 0.9:
        return {"status": 200, "data": f"Fake content from {url}"}
    else:
        return {"status": 500, "error": "Internal Server Error"}

def simulate_post_request(url, payload):
    """
    Simulate a POST request with a payload.
    """
    print(f"Sending POST request to {url} with payload {payload}")
    time.sleep(random.uniform(0.2, 0.6))
    if random.random() < 0.85:
        return {"status": 201, "message": "Resource created"}
    else:
        return {"status": 400, "error": "Bad Request"}

def simulate_put_request(url, payload):
    """
    Simulate a PUT request.
    """
    print(f"Sending PUT request to {url} with payload {payload}")
    time.sleep(random.uniform(0.2, 0.5))
    return {"status": 200, "message": "Resource updated"}

def simulate_delete_request(url):
    """
    Simulate a DELETE request.
    """
    print(f"Sending DELETE request to {url}")
    time.sleep(random.uniform(0.1, 0.4))
    if random.random() < 0.8:
        return {"status": 204, "message": "Resource deleted"}
    else:
        return {"status": 404, "error": "Resource not found"}

def batch_get_requests(url_list):
    """
    Perform a batch of GET requests.
    """
    responses = []
    for url in url_list:
        responses.append(simulate_get_request(url))
    return responses

def batch_post_requests(url_list, payload):
    """
    Perform a batch of POST requests.
    """
    responses = []
    for url in url_list:
        responses.append(simulate_post_request(url, payload))
    return responses

def retry_failed_requests(responses, retry_limit=2):
    """
    Retry failed requests up to retry_limit times.
    """
    retried = []
    for response in responses:
        retries = 0
        while retries < retry_limit and response.get('status') != 200:
            print("Retrying request...")
            response = simulate_get_request("https://retry.example.com")
            retries += 1
        retried.append(response)
    return retried

def simulate_api_tests():
    """
    Run simulated API tests.
    """
    print("\n=== Starting API Test Simulation ===")

    test_urls = [
        "https://example.com/api/resource1",
        "https://example.com/api/resource2",
        "https://example.com/api/resource3"
    ]

    print("\nGET Request Test:")
    get_responses = batch_get_requests(test_urls)
    print(f"GET Responses: {get_responses}")

    print("\nPOST Request Test:")
    post_responses = batch_post_requests(test_urls, {"sample": "data"})
    print(f"POST Responses: {post_responses}")

    print("\nRetry Failed Requests Test:")
    retried_responses = retry_failed_requests(get_responses)
    print(f"Retried GET Responses: {retried_responses}")

    print("\n=== API Test Simulation Completed ===")
