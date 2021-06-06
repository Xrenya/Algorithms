a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

def brick(a, b, c, d, e):
    if a <= d and b <= e:
        return "YES"
    elif a <= e and b <= d:
        return "YES"
    elif b <= e and c <= d:
        return "YES"
    elif b <= d and c <= e:
        return "YES"
    elif a <= d and c <= e:
        return "YES"
    elif a <= e and c <= d:
        return "YES"
    return "NO"

print(brick(a, b, c, d, e))
