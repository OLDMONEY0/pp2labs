import os

def check(path):
  if os.path.exists(path):
    print(path)
  else:
    print('path already not exists')

path = input()
check(path)