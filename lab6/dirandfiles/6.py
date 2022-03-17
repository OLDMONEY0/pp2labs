import string, os
for letter in string.ascii_uppercase:
    f = open(letter + '.txt', 'x')

f.write('new line')


f.close()