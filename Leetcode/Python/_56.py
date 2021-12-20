class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merge = [intervals[0]]
        for inter in intervals[1:]:
            if inter[0] <= merge[-1][1] and inter[1] <= merge[-1][1]:
                continue
            elif inter[0] <= merge[-1][1]:
                merge[-1] = [merge[-1][0], inter[1]]
            else:
                merge.append(inter)
        return merge
