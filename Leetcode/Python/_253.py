"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        events = []
        for i in range(len(intervals)):
            events.append([intervals[i].start, 1])
            events.append([intervals[i].end, -1])
        events.sort()
        cnt = 0
        maximum = 0
        for event in events:
            cnt += event[-1]
            if cnt > maximum:
                maximum = cnt
        return maximum
