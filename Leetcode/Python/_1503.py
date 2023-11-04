class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        left_m = -10**9
        right_m = 10**9
        if left:
            left_m = max(left)
        if right:
            right_m = min(right)
        return max(left_m, n - right_m)
