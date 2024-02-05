class MyClass:
    def getString(self):
        self.text = input()
    def printString(self):
        print(self.text)

p1 = MyClass()
p1.getString()
p1.printString()