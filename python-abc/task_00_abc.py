#!/usr/bin/env python3
"""
Module task_00_abc
This module defines an abstract base class Animal with two
subclasses: Dog and Cat. Each subclass implements the abstract
method sound to return their respective sounds.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an Animal."""

    @abstractmethod
    def sound(self):
        """Return the sound made by the animal."""
        pass


class Dog(Animal):
    """Class representing a Dog, a type of Animal."""

    def sound(self):
        """Return the sound made by the Dog."""
        return "Bark"


class Cat(Animal):
    """Class representing a Cat, a type of Animal."""

    def sound(self):
        """Return the sound made by the Cat."""
        return "Meow"
