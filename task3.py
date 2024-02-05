class Shape:
    def area():
        return 0
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        print(self.length*self.width)

rect1 = Rectangle(2,6)
rect1.area()