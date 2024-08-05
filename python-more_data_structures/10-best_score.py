#!/usr/bin/python3
def best_score(a_dictionary):
    # Verificar si el diccionario es None o está vacío
    if a_dictionary is None or not a_dictionary:
        return None
    
    # Encontrar la clave con el valor máximo
    return max(a_dictionary, key=a_dictionary.get)
