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
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        # Write your code here
        sorted_intervals = sorted(intervals, key=lambda x: x.start)
        for i in range(1, len(sorted_intervals)):
            if sorted_intervals[i - 1].end > sorted_intervals[i].start:
                return False
        return True

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        # Write your code here
        end = None
        for p in sorted(intervals, key=lambda x: x.start):
            if end:
                if end > p.start:
                    return False
                end = p.end
            else:
                end = p.end
        return True
