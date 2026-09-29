class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        for i in range(1, len(intervals)):
            if intervals[i - 1][1] <= intervals[i][0]:
                continue
            else:
                return False
        return True
