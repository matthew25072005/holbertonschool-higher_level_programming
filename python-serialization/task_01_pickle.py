#!/usr/bin/env python3
"""
Este módulo define la clase CustomObject y proporciona funciones para
serializar (guardar) y deserializar (cargar) una instancia de la clase
a/desde un archivo usando el módulo pickle.
"""
import pickle


class CustomObject:
    """Una clase personalizada con métodos para serializar y deserializar."""

    def __init__(self, name, age, is_student):
        """Inicializa un objeto personalizado."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Muestra el objeto personalizado."""
        print("Nombre: {}".format(self.name))
        print("Edad: {}".format(self.age))
        print("Es estudiante: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Serializa el objeto personalizado.

        Args:
            filename (str): El nombre del archivo donde se guardará el objeto.

        Retorna:
            None si ocurre un error, de lo contrario no retorna nada.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except (FileNotFoundError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializa el objeto personalizado.

        Args:
            filename (str): 
            El nombre del archivo desde donde se cargará el objeto.

        Returns:
            CustomObject: El objeto personalizado deserializado,
            o None si ocurre un error.
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, pickle.PickleError):
            return None
