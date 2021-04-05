"""
Дан список интов, повторяющихся элементов в списке нет. Нужно преобразовать это множество в строку, сворачивая соседние по числовому ряду числа в диапазоны. Примеры:
[1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"
[1,4,3,2] => "1-4"
[1,4] => "1,4" повторений.
"""
def sort(array: list()) -> list():
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while (i>-1) and (array[i]>key):
            array[i+1] = array[i]
            i -= 1
        array[i+1] = key
    return array

def repr(group_start: int, group_end: int) -> str():
    # Vizual representation
    if group_start == group_end:
        return "{}".format(group_start)
    return "{}-{}".format(group_start, group_end)


def transform(array) -> str():
    out_list = []
    # Return empty string if an array is empty
    if array is None:
        return ""
    # Sort array in-place with time complexity O(n**2)
    array = sort(array)
    group_start = None
    group_end = None
    for num in array:
        if group_end is None:
            group_start = num
            group_end = num
        elif group_end == num-1:
            group_end = num 
        else:
            out_list.append(repr(group_start, group_end))
            group_start = num
            group_end = num
    out_list.append(repr(group_start, group_end)) # add the last group
    return ",".join(out_list)
    
print(transform([1,4,5,6,8,9,10,12,13]))
