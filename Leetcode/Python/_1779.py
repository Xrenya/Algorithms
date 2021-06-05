class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        diff = inf
        index = -1
        coord = []
        for i, p in enumerate(points):
            if x == p[0] or y == p[1]:
                num = self.calc(x, y, p[0], p[1])
                if diff > num:
                    diff = num
                    index = i
                    coord = [p[0], p[1]]
        return index
    def calc(self, x, y, x1, y1):
        return abs(x1 - x) + abs(y1 - y)
