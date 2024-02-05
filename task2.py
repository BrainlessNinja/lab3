class Shape:
    length = 0
    def area(length):
        print(length**2)

class Square(Shape):
    def __init__(self,length):
        self.length = length
    def area(self):
        print(self.length**2)

sp1 = Shape()
sp1.area(5)
sq1 = Square(5)
sq1.area()