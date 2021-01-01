def equal(a, b, c):
    eps = 1e-10
    if abs(a + b - c) < eps:
        return "YES"
    else:
        return "NO" 
