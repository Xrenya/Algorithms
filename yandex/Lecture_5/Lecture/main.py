
def makeprefixsum(nums):
    prefixsum = [0] * (len(nums) + 1)
    for i in range(1, len(nums)+1):
        prefixsum[i] = prefixsum[i-1] + nums[i-1]
    return prefixsum

def rsq(prefixsum, l, r): # Range Sum Query
    return prefixsum[r] - prefixsum[l]
  
def countzeroes(nums, l, r):
    cnt = 0 # complexity O(NM) N - lenght of array, M - number of requests
    for i in range(i, r):
        if nums[i] == 0:
            cnt += 1
    return cnt 
