"""
Даны два массива: [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
Надо вернуть [1, 2, 2, 3] (порядок неважен)
"""
def intersection(l1, l2):
    # Time complexity O(n) + O(m) 
    hashMap = dict()
    for element in l1:
        if element in hashMap:
            hashMap[element] += 1
        else:
            hashMap[element] = 1
    
    out_array = []
    for element in l2:
        if element in hashMap:
            if hashMap[element] > 0:
                out_array.append(element)
                hashMap[element] -= 1
    return out_array
    
print(intersection([1, 2, 3, 2, 0], [5, 1, 2, 7, 3, 2])) # output: [1, 2, 3, 2]
