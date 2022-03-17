import os

WORKING_DIR = os.getcwd()

isdir = []
isfile = []

for item in os.listdir(WORKING_DIR):
    if os.path.isdir(item):
        isdir.append(item)
    if os.path.isfile(item):
        isfile.append(item)

print(isdir)
print(isfile)
print(isfile+isdir)
