#!/usr/bin/env python3

import requests
import glob

def upload_file(url, content, json=True):
    if not json:
       with open(content, 'rb') as f:
           requests.post(url, files={'file': f})
    else:
      requests.post(url, data=content)

def main():
    url = "http://localhost/upload/"
    for file in glob.glob("supplier-data/images/*.jpeg"):
        print(file)
        upload_file(url, file, json=False)

if __name__ == "__main__":
  main()
