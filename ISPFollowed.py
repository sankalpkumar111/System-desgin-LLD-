from abc import ABC ,abstractmethod

class  Shape2D(ABC):
    @abstractmethod
    def area(self):
        pass

class Shape3D(ABC):
    @abstractmethod
    def volume(self):
        pass
    
    def area(self):
        pass

class Square(Shape2D):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side*self.side

class Rectangle(Shape2D):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    
    def area(self):
        return self.length*self.width

class Cube(Shape3D):
    def __init__(self,side):
        self.side=side
    
    def area(self):
        return 6*(self.side*self.side)
    
    def volume(self):
        return self.side*self.side*self.side

cube=Cube(3)

print(cube.area())
print(cube.volume())

square=Square(3)

print(square.area())

rectangle=Rectangle(3,4)

print(rectangle.area())