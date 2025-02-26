# Palindrome-Checker

def palindrome_checker():
    s = input("what is the string you want to check? ")
    if s == s[::-1]:
        print("the string is palindrome")
    else:
        print("the string is not palindrome")

palindrome_checker()