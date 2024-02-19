class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        output = []
        start_remove, end_remove = toBeRemoved
        for start, end in sorted(intervals):
            if start > end_remove or end < start_remove:
                output.append([start, end])
            else:
                if start < start_remove:
                    output.append([start, start_remove])
                if end > end_remove:
                    output.append([end_remove, end])
        return output
