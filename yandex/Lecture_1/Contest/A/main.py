a, b = list(map(int, input().split(" ")))
condition = str(input())
def calc(a, b, condition):
    if condition == "freeze":
        if  a < b:
            return a
        else:
            return b
    elif condition == "heat":
        if  a < b:
            return b
        else:
            return a
    elif condition == "auto":
        return b
    return a
print(calc(a=a, b=b, condition=condition))
