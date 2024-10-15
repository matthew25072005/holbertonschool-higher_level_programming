#!/usr/bin/python3
"""
Task: Fetch and process posts from JSONPlaceholder
"""
import requests
import csv

# URL de la API JSONPlaceholder para obtener las publicaciones
API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """
    Fetches posts from JSONPlaceholder and prints the status code and post titles.
    """
    # Enviar solicitud GET a la API
    response = requests.get(API_URL)

    # Imprimir el código de estado de la respuesta
    print(f"Status Code: {response.status_code}")

    # Si la solicitud es exitosa (status code 200), procesar la respuesta
    if response.status_code == 200:
        # Convertir la respuesta a formato JSON
        posts = response.json()

        # Iterar sobre las publicaciones e imprimir los títulos
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """
    Fetches posts from JSONPlaceholder and saves them to a CSV file.
    """
    # Enviar solicitud GET a la API
    response = requests.get(API_URL)

    # Si la solicitud es exitosa (status code 200), procesar la respuesta
    if response.status_code == 200:
        # Convertir la respuesta a formato JSON
        posts = response.json()

        # Estructurar los datos en una lista de diccionarios
        posts_data = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]

        # Guardar los datos en un archivo CSV
        with open('posts.csv', mode='w', newline='') as csv_file:
            # Crear el escritor de CSV
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # Escribir la cabecera del CSV
            writer.writeheader()

            # Escribir las filas de datos
            writer.writerows(posts_data)

        print("Posts saved to posts.csv")


# Pruebas básicas del script en el archivo main_02_requests.py
if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
