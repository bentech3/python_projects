# Rectangle Class
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Perimeter(self):
        return 2 * (self.length + self.width)

    def Area(self):
        return self.length * self.width

    def display(self):
        print(f"Length: {self.length}")
        print(f"Width: {self.width}")
        print(f"Perimeter: {self.Perimeter()}")
        print(f"Area: {self.Area()}")


# Parallelepipede Class inheriting from Rectangle
class Parallelepipede(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def Volume(self):
        return self.length * self.width * self.height


# Example usage
rectangle = Rectangle(10, 5)
rectangle.display()

parallelepipede = Parallelepipede(10, 5, 3)
print(f"Volume of Parallel epipede: {parallelepipede.Volume()}")
