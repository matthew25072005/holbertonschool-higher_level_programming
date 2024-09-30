#!/usr/bin/python3
"""This module defines Fish, Bird, and FlyingFish classes demonstrating multiple inheritance."""

class Fish:
    """A class representing a fish."""

    def swim(self):
        """Method for fish swimming."""
        print("The fish is swimming.")

    def habitat(self):
        """Method for fish habitat."""
        print("The fish lives in water.")


class Bird:
    """A class representing a bird."""

    def fly(self):
        """Method for bird flying."""
        print("The bird is flying.")

    def habitat(self):
        """Method for bird habitat."""
        print("The bird lives in the sky.")


class FlyingFish(Fish, Bird):
    """A class representing a flying fish that inherits from Fish and Bird."""

    def swim(self):
        """Override swim method from Fish class."""
        print("The flying fish is swimming!")

    def fly(self):
        """Override fly method from Bird class."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Override habitat method to reflect its dual nature."""
        print("The flying fish lives both in water and the sky!")


# Example of testing the classes
if __name__ == "__main__":
    flying_fish = FlyingFish()
    flying_fish.swim()      # Calls the overridden swim method
    flying_fish.fly()       # Calls the overridden fly method
    flying_fish.habitat()   # Calls the overridden habitat method

    # Print the method resolution order
    print("Method Resolution Order:", FlyingFish.mro())
