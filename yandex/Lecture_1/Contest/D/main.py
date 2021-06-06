a = int(input())
b = int(input())
c = int(input())
def solve(a=a, b=b, c=c):
    if c < 0:
        return "NO SOLUTION"
    elif a == 0:
        if int(b**0.5) == c:
            return "MANY SOLUTIONS"
        else:
            return "NO SOLUTION"
    else:
        num = (c**2 - b) / a
        if is_integer_num(num):
            return int(num)
        else:
            return "NO SOLUTION"

def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False

print(solve(a=a, b=b, c=c))
