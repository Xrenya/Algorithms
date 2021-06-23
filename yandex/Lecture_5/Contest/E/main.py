with open('input.txt') as f:
    n, k = list(map(int, f.readline().split()))
    nums = list(map(int, f.readline().split()))

def trees(n, k, nums):
    treeDict = {}
    left = 0
    output = [0, n]
    for right, num in enumerate(nums):
        if num not in treeDict:
            treeDict[num] = 0
        treeDict[num] += 1
        if len(treeDict) == k:
            while treeDict[nums[left]] > 1:
                treeDict[nums[left]] -= 1
                left += 1
            if right - left < output[1] - output[0]:
                output = [left, right]
    output[0] += 1
    output[1] += 1
    return output

if __name__ == '__main__':
    ans = trees(n, k, nums)
    with open('output.txt', 'w') as file:
        file.write(f"{ans[0]} {ans[1]}")
