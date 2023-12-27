class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total = 0
        max_time = 0

        for i in range(len(colors)):
            if i > 0 and colors[i] != colors[i - 1]:
                max_time = 0
                
            total += min(max_time, neededTime[i])
            max_time = max(max_time, neededTime[i])
        
        return total


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total_time = 0
        i, j = 0, 0

        while i < len(neededTime) and j < len(neededTime):
            cur_total = 0
            cur_max = 0

            while j < len(neededTime) and colors[i] == colors[j]:
                cur_total += neededTime[j]
                cur_max = max(cur_max, neededTime[j])
                j += 1

            total_time += cur_total - cur_max
            i = j

        return total_time
