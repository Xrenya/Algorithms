class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        for idx in range(1, len(points)):
            time += max(abs(points[idx-1][0]-points[idx][0]), 
                       abs(points[idx-1][1]-points[idx][1]))
        return time
      
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        x1, y1 = points.pop()
        while points:
            x2, y2 = points.pop()
            time += max(abs(y2 - y1), abs(x2-x1))
            x1, y1 = x2, y2
        return time
