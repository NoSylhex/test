# Liskov substitution principle LSP

class Rectangle:
    def __init__(self, width, height) -> None:
        self._height = height
        self._width = width

    @property
    def area(self): return self._width * self._height

    def __str__(self) -> str:
        return f'Width: {self.width}, height: {self.height}'
    
    @property
    def width(self): return self._width
    @property
    def height(self): return self._height

    @width.setter
    def width(self, width): self._width = width
    @height.setter
    def height(self, height): self._height = height

class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value

def use_it(rc):
    w = rc.width
    rc.height = 10
    expected = int(w*10)
    print(f'Expected area of {expected}, got {rc.area}')


rc = Rectangle(2, 3)
use_it(rc)

sq = Square(5)
use_it(sq)
"""
    the use_it method works only for rectangle, 
    square breaks it because it does not respect Liskov substitution principle
    which is an interface that takes a base class should be able to take 
    this class and everything should work
"""