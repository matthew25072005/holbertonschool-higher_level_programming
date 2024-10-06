#!/usr/bin/python3
"""
Este módulo contiene una función para convertir una cadena JSON en una 
estructura de datos de Python.

El módulo utiliza el paquete estándar `json` de Python para realizar la 
deserialización, lo que convierte una cadena JSON en un objeto nativo de Python, 
como un diccionario o una lista.

Funciones:
    - from_json_string(my_str): Convierte una cadena JSON en un objeto de 
      Python.

Uso:
    Este módulo permite convertir una cadena en formato JSON en un objeto 
    nativo de Python que puede ser manipulado. No maneja excepciones en caso 
    de que la cadena JSON no represente un objeto válido.
"""

import json


def from_json_string(my_str):
    """
    Convierte una cadena JSON a un objeto de Python.
    
    Args:
        my_str: La cadena en formato JSON que será convertida.
        
    Returns:
        Un objeto de Python representado por la cadena JSON.
    """
    des_my_str = json.loads(my_str)

    return des_my_str
