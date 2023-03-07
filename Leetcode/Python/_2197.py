class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left, right = 1, min(time) * totalTrips

        def timeEnough(given_time: int) -> bool:
            actual_trips = 0
            for t in time:
                actual_trips += given_time // t
            return actual_trips >= totalTrips

        while left < right:
            m = left + (right - left) // 2
            if timeEnough(m):
                right = m
            else:
                left = m + 1
        return left
