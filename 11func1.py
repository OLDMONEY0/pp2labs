def palindrome(string):
    return string == string[::-1]
 
 
tocheck = palindrome(string=input())
 
if tocheck:
    print("True")
else:
    print("False")
