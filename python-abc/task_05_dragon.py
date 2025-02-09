#!/usr/bin/python3
"""
This is a module
"""


class SwimMixin:
    """Mixin class that provides swimming functionality."""
    
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    """Mixin class that provides flying functionality."""
    
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """Class representing a dragon that can swim and fly."""
    
    def roar(self):
        print("The dragon roars!")
