class Shape:
    def __init__(self, color= "red", filled=True):
        self.color = color
        self.filled = filled

    def getColor(self):
        return self.color
    
    def setColor(self, color):
        self.color = color

    def isFilled(self):
        return self.filled
    
    def setFilled( self, filled):
        self.filled = filled

    def __str__(self):
        return f"Shape[color={self.color}, filled={self.filled}]"
    
class Circle(Shape):
    def __init__(self, color= "red", filled=True, radius=1.0):
        super().__init__(color, filled)
        self.radius = radius
        
    def getRadius(self):
        return self.radius
    def setRadius(self, radius):
        self.radius = radius

    def getArea(self):
        import math
        return math.pi * (self.radius **2)
    
    def getPerimeter(self):
        import math
        return math.pi * 2 * self.radius
    
    def __str__(self):
        return f"Circle[color={self.color}, filled={self.filled}, radius={self.radius}]"
    
class Rectangle(Shape):
    def __init__(self, color= "red", filled=True, width=1.0, length=1.0 ):
        super().__init__(color, filled)
        self.width = width
        self.length = length

    def getWidth(self):
        return self.width
    
    def setWidth(self, width):
        self.width = width

    def getLength(self):
        return self.length

    def setLength(self, length):
        self.length = length

    def getArea(self):
        return self.width * self.length
    
    def getPerimeter(self):
        return 2*self.width + 2*self.length
    
    def __str__(self):
        return f"Rectangle[color={self.color}, filled={self.filled}, width={self.width}, length={self.length}]"
    
class Square(Rectangle):
    def __init__(self, side=1.0, color="red", filled=True):
        super().__init__(color, filled, side, side)

    def getSide(self):
        return self.width
    
    def setSide(self, side):
        self.width = side
        self.length = side

    def setWidth(self, side):
        self.setSide(side)
    
    def setLength(self, length):
        self.setSide(side)
        
    def __str__(self):
        return f"Square[color={self.color}, filled={self.filled}, side={self.width}]"
    
circle1 = Circle("blue", True, 1.0)
print(circle1)  

rectangle1 = Rectangle(width=4.0, length=6.0, color="green", filled=True)
print(rectangle1)  

square1 = Square(side=3.0, color="yellow", filled=True)
print(square1) 

