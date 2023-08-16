# Task
# Write a function which return True if a sentence is anagram,
# only letters should be compared
# Examples:
# Madam -> True
# Madam! -> True
# Madam mad -> False
# Let lil 5 tel? -> True

def is_anagram(s):
    left, right = 0, len(s) - 1
    while left <= right:
        if not s[left].isalpha():
            left += 1
        elif not s[right].isalpha():
            right -= 1
        elif s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1
    return True
