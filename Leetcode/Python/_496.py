class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        for i in nums1:
            cur = -1
            flag = False
            for index, j in enumerate(nums2):
                if i == j:
                    flag = True
                if flag:
                    if j > i:
                        cur = j
                        break
            output.append(cur)
        return output
