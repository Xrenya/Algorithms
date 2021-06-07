n = int(input())
array = list(map(int, input().split()))

def is_sym(array):
    i = 0
    j = len(array) - 1
    while j - i >= 1:
        if array[i] ==  array[j]:
            i += 1
            j -= 1
        else:
            return False
    return True

def find_pos(array):
    now = array[-1]
    induces = []
    for i in range(len(array)):
        if array[i] == now:
            induces.append(i)
    return induces

def verify(array, induces):
    for idx in induces:
        mirror_arr = array[:idx][::-1]
        full_array = array  + mirror_arr
        if is_sym(full_array):
            return mirror_arr

if is_sym(array):
    print(0)
else:
    induces = find_pos(array)
    mirror_arr = verify(array, induces)
    print(len(mirror_arr))
    print(" ".join(list(map(str, mirror_arr))))
