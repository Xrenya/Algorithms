array = [int(x) for x in input().split(" ")]
def monoton(array):
    if len(array) < 1:
        return "NO"
    elif len(array) == 1:
        return "YES"
    for i in range(1, len(array)):
        if array[i] <= array[i-1]:
            return "NO"
    return "YES"
print(monoton(array=array))
