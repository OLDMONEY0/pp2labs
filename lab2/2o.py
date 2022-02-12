a = {
    'ONE' : '1',
    'TWO' : '2',
    'THR' : '3', 
    'FOU' : '4', 
    'FIV' : '5', 
    'SIX' : '6', 
    'SEV' : '7', 
    'EIG' : '8', 
    'NIN' : '9',
    'ZER' : '0'
}

s = input()

def dec(s):
    for i, j in a.items():
        s = s.replace(i, j)
    x = s.index('+')
    sum = int(s[:x]) + int(s[x + 1:])
    return str(sum)

def enc(sum):
    for i, j in a.items():
        sum = sum.replace(j, i)
    print(sum)

sum = dec(s)
enc(sum)