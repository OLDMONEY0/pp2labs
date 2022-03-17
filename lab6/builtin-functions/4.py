import math, time 
s = int(input())
timer = int(input())
time.sleep(timer/1000)

print("Square root of",s,"after",timer,"milliseconds is",math.sqrt(s))
