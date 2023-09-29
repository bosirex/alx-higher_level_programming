#!/usr/bin/python3
"""Script that sends a POST request with data in the variable q"""

import requests
from sys import argv
if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": argv[1][0] if len(argv) > 1 else ""}
    res = requests.post(url, data=data)
    try:
        k = res.json()
        if not k:
            print("No result")
        else:
            print("[{}] {}".format(k.get("id"), k.get("name")))
    except ValueError:
        print("Not a valid JSON")
