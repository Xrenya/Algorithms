def equal(a, b, c):
    eps = 1e-10
    if abs(a + b - c) < eps:
        return "YES"
    else:
        return "NO" 
a = float(input())
b = float(input())
c = float(input())
equal(a, b, c)
