#!/usr/bin/python3
"""
script fetches https://alx-intranet.hbtn.io/status
"""
import requests
if __name__ == '__main__':
    req = requests.get('https://alx-intranet.hbtn.io/status')
    text = req.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))
