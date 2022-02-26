import datetime
a = datetime.datetime(2021,7,26,13,7,30)
b = datetime.datetime(2021,7,25,11,28,30)
c=a-b
seconds = c.total_seconds() 
print(seconds)