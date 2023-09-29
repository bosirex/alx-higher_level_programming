#!/usr/bin/python3
"""
script takes your Github credentials and uses the GitHub API
to dispaly your ID.
"""
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://api.github.com/user'
    res = requests.get(url, auth=(argv[1], argv[2]))
    try:
        print(res.json().get("id"))
    except ValueError:
        print("Not a valid JSON")
