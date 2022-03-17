import os
s = input()
print('Exist:', os.access(s , os.F_OK))
print('Readable:', os.access(s , os.R_OK))
print('Writable:', os.access(s , os.W_OK))
print('Executable:', os.access(s , os.X_OK))

def check(s):
  if os.path.exists(s):
    print(s)
  else:
    print('path already not exists')

check(s)
os.remove(s)