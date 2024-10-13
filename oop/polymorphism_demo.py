import math

# Base Class: Shape
class Shape:
    def area(self):
        """Method to be overridden in derived classes."""
        raise NotImplementedError("Subclasses must override the area() method.")

# Derived Class: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize the rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of a rectangle."""
        return self.length * self.width

# Derived Class: Circle
class Circle(Shape):
    def __init__(self, radius):
        """Initialize the circle with a radius."""
        self.radius = radius

    def area(self):
        """Calculate the area of a circle using π * radius^2."""
        return math.pi * (self.radius ** 2)
