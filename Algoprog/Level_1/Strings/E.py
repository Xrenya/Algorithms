string = input()

def palindrome(string):
    return "yes" if string[::-1] == string else "no"

palindrome(string)
