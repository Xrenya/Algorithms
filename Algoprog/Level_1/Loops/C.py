num = int(input())

def square(n):
   output = 0
   while n > 0:
       output += n ** 2
       n -= 1
   return output

num = int(input())

def square_recursive(n):
   if n == 0:
       return n
   else:
       return n**2 + square(n-1)

print(square(num), square_recursive(num))
