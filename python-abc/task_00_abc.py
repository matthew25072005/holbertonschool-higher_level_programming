#!/usr/bin/python3
"""
This is a module
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    an abstract class named Animal
    """
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    """
    subclasse of Animal
    """
    def sound(self):
        return "Bark"

class Cat(Animal):
    """
    subclasse of Animal
    """
    def sound(self):
        return "Meow"
