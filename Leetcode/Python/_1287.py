class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        c = len(arr) // 4 + 1
        counter = 1
        prev = arr[0]
        for v in arr[1:]:
            if prev == v:
                counter += 1
            else:
                counter = 1
                prev = v
            if counter >= c:
                return prev
        if counter >= c:
            return prev
        return -1
