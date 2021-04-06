class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        count = 0
        maxLen = -inf
        for h, w in rectangles:
            if h<w:
                minLen = h
            else:
                minLen = w
            if maxLen<minLen:
                maxLen = minLen
                count = 1
            elif maxLen == minLen:
                count += 1
        return count
