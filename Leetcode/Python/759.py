"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        schedule_time = defaultdict(int)
        flat_schedule = []

        for intervals in schedule:
            for interval in intervals:
                start = interval.start
                end = interval.end
                flat_schedule.append((start, 1))
                flat_schedule.append((end, -1))

        flat_schedule.sort(key=lambda x: (x[0], -x[1]))
        employee = 0
        for time, emp in flat_schedule:
            employee += emp
            schedule_time[time] = employee

        output = []
        last = -1
        for key in sorted(schedule_time.keys()):
            if last != -1:
                interv = Interval(last, key)
                output.append(interv)
                last = -1
            elif schedule_time[key] == 0:
                last = key
        return output
