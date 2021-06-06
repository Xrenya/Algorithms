a = int(input())
b = int(input())
c = int(input())
def calc(a, b, c):
    if a + b <= c:
        return "NO"
    if a + c <= b:
        return "NO"
    if c + b <= a:
        return "NO"
    return "YES"
print(calc(a=a, b=b, c=c))
