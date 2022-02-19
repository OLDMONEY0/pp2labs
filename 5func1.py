def perm(s, per):
    if len(s) == 0:
        print(per)
        return 
    for i in range(len(s)):
        fixed = s[0:i] + s[i+1:]
        perm(fixed, per+s[i])