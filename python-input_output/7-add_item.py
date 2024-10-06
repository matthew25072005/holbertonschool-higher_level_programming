#!/usr/bin/python3
"""
Este módulo añade todos los argumentos pasados a una lista de Python y los
guarda en un archivo usando una representación JSON.
"""
import sys
import os
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

# Nombre del archivo donde se guardará la lista en formato JSON
filename = "add_item.json"

# Verifica si el archivo ya existe para cargar la lista, si no, crea una nueva
if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Agrega los argumentos pasados desde la línea de comandos a la lista
my_list.extend(sys.argv[1:])

# Guarda la lista actualizada en el archivo JSON
save_to_json_file(my_list, filename)
