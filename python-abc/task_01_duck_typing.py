class Circle(Shape):
    """Class representing a Circle, inheriting from Shape."""

    def __init__(self, radius):
        """Initialize the Circle with a radius.
        
        Args:
            radius (float): The radius of the Circle.
        
        Raises:
            ValueError: If radius is not a positive number.
        """
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.__radius = radius

    def area(self):
        """Calculate and return the area of the Circle."""
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        """Calculate and return the perimeter of the Circle."""
        return 2 * math.pi * self.__radius
