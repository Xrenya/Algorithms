array = list(map(int, input().split()))
 
def unique(array):
    hashMap = {}
    for num in array:
        if num not in hashMap:
            hashMap[num] = 0
        hashMap[num] += 1
    return len(hashMap)

print(unique(array))
