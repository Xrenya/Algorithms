class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))

        tmp = []
        tmp.append(intervals[0])
        output: int = 0
        for i in range(1, len(intervals)):
            if tmp[-1][1] >= intervals[i][1] and tmp[-1][0] <= intervals[i][0]:
                continue
            else:
                tmp.append(intervals[i])
        return len(tmp)
