import math
class Point():
    def __init__(self, x0, x1, y0, y1):
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1
    def show(self):
        print(f'x0 = {self.x0}, x1 = {self.x1}, y0 = {self.y0}, y1 = {self.y1}')
    def move(self):
        self.x0, self.x1, self.y0, self.y1 = map(int, input("Move 4 points \n").split()) 
    def dis(self):
        self.distace = math.sqrt((self.x0 - self.x1)**2 + (self.y0 - self.y1)**2)
        print(f'Distance between two points is {self.distace}') 
print('Enter 4 points(x0, x1, y0, y1): ')
x0, x1, y0, y1 = map(int, input().split())
points = Point(x0, x1, y0, y1)
points.dis()
points.move()
points.show()
points.dis()