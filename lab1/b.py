a =str(input())
b = 0
for x in a:
    b += ord(x)
if  b > 300 :
    print("It is tasty!")
if  b < 300 :
    print("Oh, no!")    
