#!/usr/bin/python3
"""
Python script that sends a request to the URL and
displays the value of a variable in the response header
"""
import requests
import sys
from requests.exceptions import RequestException


if __name__ == "__main__":
    try:
        r = requests.get(sys.argv[1])
        r.raise_for_status()
        print(r.headers['X-Request-Id'])
    except RequestException:
        pass
