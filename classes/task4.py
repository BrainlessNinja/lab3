import math
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def show(self):
        print(f"[{self.x},{self.y}]")
    def move(self):
        self.x = int(input("Enter x: "))
        self.y = int(input("Enter y: "))
    def dist(self):
        x1 = int(input("Enter second x: "))
        y1 = int(input("Enter second y: "))
        distance = math.sqrt(math.pow((x1-self.x),2) + math.pow((y1-self.y),2))
        print(distance)

p1 = Point(0,0)
p1.show()
p1.move()
p1.dist()