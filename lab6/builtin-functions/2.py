def check(string):
    upper_case = 0
    lower_case = 0
    for i in string:
        for ascii in range(65, 91):
            if chr(ascii)==i:
                upper_case += 1
    for j in string:
        for ascii2 in range(97, 123):
            if chr(ascii2)==j:
                lower_case += 1
    print(upper_case , lower_case)

check(string = input())

