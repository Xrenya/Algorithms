def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    pivot = random.randint(0, len(nums) - 1) # pivot = len(nums) // 2
    left = merge_sort(nums[:pivot])
    print(left)
    right = merge_sort(nums[pivot:])
    print(right)
    return merge(left, right)
    
def merge(left, right):
    l = r = 0
    output = []
    while l < len(left) and r < len(right):
        if left[l] <  right[r]:
            output.append(left[l])
            l += 1
        else:
            output.append(right[r])
            r += 1
            
    output.extend(left[l:])
    output.extend(right[r:])
    return output

nums = [4,1,10,3]

print(merge_sort(nums))
