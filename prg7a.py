import math
class Shape:
    def area(self):
        pass
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius**2
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
# Creating instances of the classes
triangle = Triangle(int(input("enter the base")), int(input("Enter the height:")))
circle = Circle(int(input("enter the radius:")))
rectangle = Rectangle(int(input("enter the length")),int(input("enter the bredth")))
# Calculating and printing the areas
print("Area of the Triangle:", triangle.area())
print("Area of the Circle:", circle.area())
print("Area of the Rectangle:", rectangle.area())