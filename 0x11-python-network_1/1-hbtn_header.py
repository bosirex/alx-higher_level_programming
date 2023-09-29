#!/usr/bin/python3
"""
script takes in a URL, sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response
"""
import urllib.request as request
if __name__ == "__main__":
    from sys import argv
    req = request.Request(argv[1])
    with request.urlopen(req) as r:
        print(r.headers.get('X-Request-Id'))
