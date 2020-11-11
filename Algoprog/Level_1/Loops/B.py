num = int(input())

def factorial(num):
    output = 1
    while num>0:
        output *= num
        num -= 1
    return output

def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

recur_factorial(num)

print(factorial(num), recur_factorial(num))
