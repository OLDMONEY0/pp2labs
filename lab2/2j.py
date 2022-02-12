arr_emails = []
x = int(input())
for i in range(x):
    emails = input()
    arr_emails.append(emails)

right = []

for names in arr_emails:
    upper = 0
    lower = 0
    number = 0 
    for arip in names:
            if arip.isupper():
                upper += 1
            elif arip.islower():
                lower += 1
            elif arip.isdigit():
                number +=1
    if upper > 0 and lower > 0 and number>0:
        right.append(names)
        
right = sorted(set(right))
print(len(right))
for l in right:
    print(l)
    




             
