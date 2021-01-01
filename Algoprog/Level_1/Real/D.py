def run(x, y):
    days = 1
    while x < y:
        print(x)
        x *= 1.7
        days += 1
    return days-1
x, y = [float(i) for i in input().split()]
run(x, y)
