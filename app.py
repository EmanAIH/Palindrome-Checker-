# Palindrome-Checker

def palindrome_checker(s):
    s = input("what is the string you want to check")
    if s == s[::-1]:
        print("the function is palindrome")
    else:
        ("the function is not palindrome")