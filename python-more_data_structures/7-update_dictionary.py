#!/usr/bin/python3

# Importar las funciones desde sus respectivos módulos
update_dictionary = __import__('7-update_dictionary').update_dictionary
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

if __name__ == "__main__":
    a_dictionary = {
        'language': "C",
        'number': 89,
        'track': "Low level"
    }
    
    # Actualizar el diccionario y mostrar el resultado
    new_dict = update_dictionary(a_dictionary, 'language', "Python")
    print_sorted_dictionary(new_dict)
    
    print("--")
    
    print_sorted_dictionary(a_dictionary)

    print("--")
    print("--")
    
    # Añadir un nuevo elemento al diccionario y mostrar el resultado
    new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
    print_sorted_dictionary(new_dict)
    
    print("--")
    
    print_sorted_dictionary(a_dictionary)
