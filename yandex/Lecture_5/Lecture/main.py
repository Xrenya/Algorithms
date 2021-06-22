
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

# Faster solution O(N+M)
def makeprefixsum(nums):
    prefixsum = [0] * (len(nums) + 1)
    for i in range(1, len(nums)+1):
        if nums[i-1] == 0:
            prefixsum[i] = prefixsum[i-1] + 1
        else:
            prefixsum[i] = prefixsum[i-1]
    return prefixsum

def countzeroes(nums, l, r):
    return prefixsum[r] - prefixsum[l]

# O(n**3)
def countzerossumranges(nums):
    cntranges = 0
    for i in range(len(nums)): # Left boundary
        for j in range(i+1, len(nums)+1): # Right boundary
            rangesum = 0
            for k in range(i, j):
                rangesum += nums[k]
            if rangesum == 0:
                cntranges += 1
    return cntranges

# O(n)
def countprefixsum(nums):
    prefixsumbyvalue = {0: 1}
    nowsum = 0
    for now in nums:
        nowsum += now
        if nowsum not in prefixsumbyvalue:
            prefixsumbyvalue[nowsum] = 0
        prefixsumbyvalue[nowsum] += 1
    return prefixsumbyvalue

def countzerossumrange(prefixsumbyvalue):
    cntranges = 0
    for nowsum in prefixsumbyvalue:
        cntsum = prefixsumbyvalue[nowsum]
        cntranges += cntsum * (cntsum - 1) // 2
    return cntranges

# O(n*n)
def cntpairswithdiffgtk(sortednums, k):
    contpairs = 0
    for first in range(len(sortednums)):
        for last in range(first, len(sortednums)):
            if sortednums[last] - sortednums[first] > k:
                contpairs += 1
    return contpairs
# cntpairswithdiffgtk([1,3,5,6], 3) -> 2

# O(n)
def cntpairswithdiffgtk(sortednums, k):
    contpairs = 0
    last = 0
    for first in range(len(sortednums)):
        while last < len(sortednums) and sortednums[last] - sortednums[first] <= k:
            last += 1
        contpairs += len(sortednums) - last
    return contpairs

def merge(nums1, nums2):
    merged = [0] * len(nums1) + [0] * len(nums2)
    first1 = first2 = 0
    inf = max(nums1[-1], nums2[-1]) + 1
    nums1.append(inf)
    nums2.append(inf)
    for k in range(len(nums1) + len(nums2) - 2):
        if nums1[first1] <= nums2[first2]:
            merged[k] = nums1[first1]
            first1 += 1
        else:
            merged[k] = nums2[first2]
            first2 += 1
    nums1.pop()
    nums2.pop()
    return merged

def mergebetter(nums1, nums2):
    merged = [0] * len(nums1) + [0] * len(nums2)
    first1 = first2 = 0
    for k in range(len(nums1) + len(nums2)):
        if (first1 != len(nums1)) and (first2 == len(nums2) or nums1[first1] < nums2[first2]):
            merged[k] = nums1[first1]
            first1 += 1
        else:
            merged[k] = nums2[first2]
            first2 += 1
    return merged
