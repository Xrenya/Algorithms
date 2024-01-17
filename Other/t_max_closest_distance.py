class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        max_dist = 0
        cur_dist = 0
        prev = -1
        for i in range(len(seats)):
            if seats[i] == 0:
                cur_dist += 1
            else:
                if prev == -1:
                    max_dist = max(max_dist, cur_dist)
                else:
                    max_dist = max(max_dist, math.ceil(cur_dist / 2))
                cur_dist = 0
                prev = i

        if cur_dist:
            max_dist = max(max_dist, cur_dist)
        return max_dist


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        n = len(seats)
        prefix = [n] * n
        suffix = [n] * n

        dist = n
        for i in range(n):
            if seats[i]:
                prefix[i] = 0
            else:
                prefix[i] = prefix[i - 1] + 1

            if seats[n - 1 - i]:
                suffix[n - 1 - i] = 0
            else:
                if i > 0:
                    suffix[n - 1 - i] = suffix[n - i] + 1
        dist = -float("inf")
        for i in range(n):
            dist = max(dist, min(prefix[i], suffix[i]))
        return dist
