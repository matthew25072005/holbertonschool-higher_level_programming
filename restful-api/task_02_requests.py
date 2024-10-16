#!/usr/bin/python3

import requests
import csv

def fetch_and_print_posts():
    """
    Fetch posts from JSONPlaceholder and print the status code and titles.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()
        
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    """
    Fetch posts from JSONPlaceholder and save them in a CSV file.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    
    if response.status_code == 200:
        posts = response.json()
        
        data_to_save = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]
        
        with open('posts.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            
            writer.writeheader()
            
            writer.writerows(data_to_save)

fetch_and_print_posts()
fetch_and_save_posts()
