#!/usr/bin/python3
"""This module defines mixins for swimming and flying, and a Dragon class that uses them."""

class SwimMixin:
    """Mixin class that provides swimming functionality."""
    
    def swim(self):
        """Method to simulate swimming."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class that provides flying functionality."""
    
    def fly(self):
        """Method to simulate flying."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Class representing a dragon that can swim and fly."""
    
    def roar(self):
        """Method for the dragon to roar."""
        print("The dragon roars!")


# Example of testing the classes
if __name__ == "__main__":
    dragon = Dragon()
    dragon.swim()  # Calls the swim method from SwimMixin
    dragon.fly()   # Calls the fly method from FlyMixin
    dragon.roar()  # Calls the roar method from Dragon
