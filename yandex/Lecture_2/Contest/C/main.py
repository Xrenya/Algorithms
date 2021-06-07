N = int(input())
array = [int(x) for x in input().split()]
target = int(input())
def find(array, target):
    dif = abs(target - array[0])
    ans = array[0]
    for num in array[1:]:
        if abs(target - num) < dif:
            ans = num
            dif = abs(target - num)
    return ans
            
print(find(array, target))
