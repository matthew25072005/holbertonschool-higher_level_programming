#!/usr/bin/python3
"""
Este módulo contiene una función para convertir una cadena JSON en una
estructura de datos de Python.


El módulo utiliza el paquete estándar `json` de Python para realizar la
deserialización, lo que convierte una cadena JSON en un objeto nativo de
Python,
como un diccionario o una lista.


Funciones:
    - from_json_string(my_str): Convierte una cadena JSON en un objeto de
      Python.


Uso:
    Este módulo permite convertir una cadena en formato JSON en un objeto
    nativo de Python que puede ser manipulado. No maneja excepciones en caso
    de que la cadena JSON no represente un objeto válido.
"""

import sys
import os
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = "add_item.json"

if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

my_list.extend(sys.argv[1:])
save_to_json_file(my_list, filename)
