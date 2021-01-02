n = int(input())

def factorial(n):
    if n == 1:
        return n
    else:
        return 1/n + factorial(n-1)
        
factorial(n)
