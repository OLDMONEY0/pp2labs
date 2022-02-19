class s():
    def __init__(self):
        self.asd = ""
        
    def getString(self):
        self.asd = input()
        
    def printString(self):
        print(self.asd.upper())

asd = s()
asd.getString()
asd.printString()