class HeapMin:
    def __init__(self):
        self.a = []
        self.size = 0

    def push(self, n):
        self.a.append(n)
        self.size += 1
        i = self.size - 1
        while i > 0 and self.a[i] < self.a[(i - 1) // 2]:
            self.a[i], self.a[(i - 1) // 2] = self.a[(i - 1) // 2], self.a[i]
            i = (i - 1) // 2

    def pop(self):
        self.a[-1], self.a[0] = self.a[0], self.a[-1]
        min_n = self.a.pop()
        self.size -= 1
        i = 0
        while 2 * i + 1 < self.size:
            j = 2 * i + 1
            if 2 * i + 2 < self.size and self.a[j] > self.a[2 * i + 2]:
                j = 2 * i + 2
            if self.a[i] < self.a[j]:
                break
            self.a[i], self.a[j] = self.a[j], self.a[i]
            i = j
            
            
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])

        heap = HeapMin()
        heap.push(intervals[0][1])

        for i in intervals[1:]:
            if heap.a[0] <= i[0]:
                heap.pop()

            heap.push(i[1])
        return heap.size
        
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
