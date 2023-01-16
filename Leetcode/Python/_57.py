class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l = bisect.bisect_left([x[1] for x in intervals],newInterval[0])
        r = bisect.bisect_right([x[0] for x in intervals],newInterval[1])
        
        if l < len(intervals):
            newInterval[0] = min(newInterval[0],intervals[l][0])
            
        if r > 0:
            newInterval[1] = max(newInterval[1],intervals[r-1][1])
            
        return intervals[:l] + [ newInterval ] + intervals[r:]
      
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s1, e1 = newInterval
        output = []
        index = 0
        for i, (s, e) in enumerate(intervals):
            if s < s1:
                output.append([s, e])
            else:
                index = i
                break

        if len(output) == 0 or output[-1][1] < s1:
            output.append([s1, e1])
        else:
            output[-1][1] = max(output[-1][1], e1)

        for s, e in intervals[index:]:
            if output[-1][1] < s:
                output.append([s, e])
            else:
                output[-1][1] = max(output[-1][1], e)

        return output
