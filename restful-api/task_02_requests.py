#!/usr/bin/python3

import requests

def fetch_and_print_posts():
    """
    look for posts from JSONPlaceholder and prints the status code and post titles.
    """
    info = requests.get("https://jsonplaceholder.typicode.com/posts")
    print (info.status_code)
    if info.status_code == 200:
        datos = info.json()
        for post in datos:
            print(post['title'])

def save_data():
    info = requests.get("https://jsonplaceholder.typicode.com/posts")
