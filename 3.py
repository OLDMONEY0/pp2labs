class Shape:
    def __init__(self, area):
        self.area = 0
class Rectangle(Shape):
    def __init__(self, length, width, area):
        self.length = length
        self.width = width
        super().__init__(area)

    def getArea(self):
        return self.area, self.length * self.width
    
l = int(input())
w = int(input())
R = Rectangle(l, w, 0)
print(*R.getArea())