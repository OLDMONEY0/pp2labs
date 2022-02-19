class Shape:
    def __init__(self, area):
        self.area = 0
class Square(Shape):
    def __init__(self, length, area):
        self.length = length
        super().__init__(area)
    def getArea(self):
        return self.area, self.length * self.length
n=int(input())
s = Square(n, 0)
print(*s.getArea())