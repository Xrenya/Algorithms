class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x0 = max(rec1[0], rec2[0])
        y0 = max(rec1[1], rec2[1])
        x1 = min(rec1[2], rec2[2])
        y1 = min(rec1[3], rec2[3])
        return (x0 < x1 and y0 < y1)
