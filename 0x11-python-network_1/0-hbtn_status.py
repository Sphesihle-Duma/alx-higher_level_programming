#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status """
import urllib.request
import urllib.error  # Import the urllib.error module for error handling


if __name__ == "__main__":
    try:
        with urllib.request.urlopen('https://intranet.hbtn.io/status') as r:
            res = r.read()
            print('Body response:')
            print('\t- type: {}'.format(type(res)))
            print('\t- content length: {}'.format(len(res)))
            print('\t- utf8 content: {}'.format(res.decode("utf-8")))
    except urllib.error.URLError as e:
        print(f"Error: {e}")
