array = [int(x) for x in input().split(" ")]
def find(array):
    cnt = 0
    if len(array) < 1:
        return 0
    for i in range(1, len(array)-1):
        if array[i-1] < array[i] and array[i] > array[i+1]:
            cnt += 1
    return cnt
            
print(find(array))
