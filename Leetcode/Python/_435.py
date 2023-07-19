class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count = 0
        k = -float("inf")

        for s, e in intervals:
            if s >= k:
                k = e
            else:
                count += 1
        return count
