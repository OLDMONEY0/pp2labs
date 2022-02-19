def func(lst):
    cnt = ""
    for i in lst:
        if i == '0' or i == '7':
            cnt += i
            if '007' in cnt:
                return True
            return False

lst = input().split()
print(func(lst))