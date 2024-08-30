class Circle:
    def __init__(self, radius=1.0, color="red"):
        self.radius = radius
        self.color = color
    
    def getRadius(self):
        return self.radius
    
    def setRadius(self, radius):
        self.radius = radius
    
    def getColor(self):
        return self.color
    
    def setColor(self, color):
        self.color = color

    def getArea(self):
        import math
        return math.pi * (self.radius **2)
    
    def __str__(self):
        return f"Circle[radius={self.radius}, color={self.color}]"
    
class Cylinder(Circle):
    def __init__(self, radius=1.0, color="red", height=1.0):
        super().__init__(radius, color)
        self.height = height

    def getHeight(self):
        return self.height
    
    def setHeight(self, height):
        self.height = height

    def getVolume(self):
        return self.getArea() * self.height
    
circle1 = Circle(5,"blue")
print(circle1)
print("Area: ", circle1.getArea())

cylinder1 = Cylinder()
print(cylinder1)
print("Volumen: ", cylinder1.getVolume())

