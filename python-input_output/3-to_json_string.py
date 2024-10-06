#!/usr/bin/python3
"""
Este módulo contiene una función para convertir un objeto de Python a su
representación en formato JSON.

El módulo utiliza el paquete estándar `json` de Python para realizar la
conversión de objetos a cadenas JSON.

Funciones:
    - to_json_string(my_obj): Convierte un objeto de Python a una cadena en
      formato JSON.

Uso:
    Este módulo puede ser usado para convertir cualquier objeto serializable
    en una cadena JSON. Si el objeto no es serializable, se lanzará un error,
    aunque no es necesario manejar las excepciones explícitamente.
"""

import json


def to_json_string(my_obj):
    """
    Convierte un objeto de Python a su representación en formato JSON.
        Args:
        my_obj: El objeto de Python a ser convertido a formato JSON.
        Returns:
        Una cadena que representa el objeto en formato JSON.
    """
    # Convertir el objeto a una cadena JSON
    objeto_json = json.dumps(my_obj)
    # Devolver la representación en JSON
    return objeto_json
