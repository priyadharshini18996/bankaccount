import math
 
class Shape:
 
    def __init__(self, color='red'):
        self.__color = color
       
    def get_color(self):
        return self.__color
 
    def set_color(self, color):
        self.__color = color
 
    
   
class Rectangle(Shape):
 
    def __init__(self, length, breadth):
        super().__init__()
        self.__length = length
        self.__breadth = breadth
 
    def get_length(self):
        return self.__length
 
    def set_length(self, length):
        self.__length = length
 
    def get_breadth(self):
        return self.__breadth
 
    def set_breadth(self, breadth):
        self.__breadth = breadth
 
    def get_area(self):
        return self.__length * self.__breadth
 
    def get_perimeter(self):
        return 2 * (self.__length + self.__breadth)
 
 
class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius
 
    def get_radius(self):
        return self.__radius
 
    def set_radius(self, radius):
        self.__radius = radius
 
    def get_area(self):
        return math.pi * self.__radius ** 2
 
    def get_perimeter(self):
        return 2 * math.pi * self.__radius
 
 
r = Rectangle(0.5, 0.5)
 
print("Area of rectangle :", r.get_area())
print("Perimeter of rectangle :", r.get_perimeter())
print("Color of rectangle :", r.get_color())
# r1.set_color("orange")

 
c = Circle(2)
 
print("\nArea of circle c:", format(c.get_area(), "0.2f"))
print("Perimeter of circle c:", format(c.get_perimeter(), "0.2f"))
print("Color of circle c:", c.get_color())
# c1.set_color("blue")
