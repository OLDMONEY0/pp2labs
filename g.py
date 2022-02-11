def rec_deci(x):
    
    if x == 1 or x == 0:
        return x
    
    l = len(str(x))
    firstDigit = x//pow(10,l-1)
    
    return (pow(2,l-1) * firstDigit)+ rec_deci(x%pow(10,l-1))

binary = int(input())
q = rec_deci(binary)

print(q)