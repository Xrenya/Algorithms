array = []
val = int(input())

while val != -2000000000:
    array.append(val)
    val = int(input())

def contant(array):
    now = array[0]
    for num in array[1:]:
        if now != num:
            return 0
    return 1

def ascending(array):
    now = array[0]
    for num in array[1:]:
        if now < num:
            now = num
        else:
            return 0
    return 1

def weak_ascending(array):
    now = array[0]
    for num in array[1:]:
        if now <= num:
            now = num
        else:
            return 0
    return 1

def descending(array):
    now = array[0]
    for num in array[1:]:
        if now > num:
            now = num
        else:
            return 0
    return 1


def weak_descending(array):
    now = array[0]
    for num in array[1:]:
        if now >= num:
            now = num
        else:
            return 0
    return 1


def array_type(array):
    if contant(array):
        return "CONSTANT"
    if ascending(array):
        return "ASCENDING"
    if weak_ascending(array):
        return "WEAKLY ASCENDING"
    if descending(array):
        return "DESCENDING"
    if weak_descending(array):
        return "WEAKLY DESCENDING"
    else:
        return "RANDOM"

print(array_type(array))
