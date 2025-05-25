from enum import Enum
import requests
import json

class RestMethod(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"

    def __str__(self):
        return self.value
 
def send_get_request(url: str):
    return send_request(RestMethod.GET, url)

def send_post_request(url: str, data={}, headers={}):
    return send_request(RestMethod.POST, url, data, headers)

def send_request_with_json(url: str, data: dict, headers={}):
    headers = {**headers, "Content-Type": "application/json"}
    return send_request(RestMethod.POST, url, json.dumps(data), headers)
    
def send_request(method: RestMethod, url: str, data={}, headers={}):
    timeout = (3, 10)  # Connect timeout, read timeout
    if method == RestMethod.GET:
        response = requests.get(url, headers=headers, timeout=timeout)
    elif method == RestMethod.POST:
        response = requests.post(url, json=data, headers=headers, timeout=timeout)
    elif method == RestMethod.PUT:
        response = requests.put(url, json=data, headers=headers, timeout=timeout)
    elif method == RestMethod.DELETE:
        response = requests.delete(url, headers=headers, timeout=timeout)
    else:
        raise ValueError(f"Unsupported HTTP method: {method}")
    
    # Check if the response is successful
    if not response.ok:
        raise requests.HTTPError(f"HTTP error occurred: {response.status_code} - {response.text}")
    # Attempt to parse JSON response if applicable
    try:
       return response.json()
    except ValueError:
        # If the response is not JSON, return the text
        return response.text