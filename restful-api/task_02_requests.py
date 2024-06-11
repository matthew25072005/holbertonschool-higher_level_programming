#!/usr/bin/python3

# Importamos las bibliotecas necesarias
import requests
import json
import csv

# Definimos la URL de la API
url = "https://jsonplaceholder.typicode.com/posts"

def fetch_and_print_posts():
    # Hacemos una solicitud GET a la API
    response = requests.get(url)

    # Imprimimos el código de estado de la respuesta
    print("Status Code:", response.status_code)

    # Si la solicitud fue exitosa
    if response.status_code == 200:
        # Convertimos los datos obtenidos en un objeto JSON
        data = response.json()

        # Iteramos a través de los datos JSON e imprimimos los títulos de todas las publicaciones
        for post in data:
            print(post["title"])

def fetch_and_save_posts():
    # Hacemos una solicitud GET a la API
    response = requests.get(url)

    # Si la solicitud fue exitosa
    if response.status_code == 200:
        # Convertimos los datos obtenidos en un objeto JSON
        data = response.json()

        # Creamos una lista de diccionarios, donde cada diccionario representa una publicación
        posts = [{"id": post["id"], "title": post["title"], "body": post["body"]} for post in data]

        # Escribimos estos datos en un archivo CSV llamado posts.csv
        with open("posts.csv", "w", newline="", encoding='utf-8') as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(posts)

# Llamamos a las funciones
fetch_and_print_posts()
fetch_and_save_posts()
