class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 0
        right = max(piles) + 1
        while left < right - 1:
            speed = left + (right - left) // 2
            hours_spend = 0
            for pile in piles:
                hours_spend += math.ceil(pile / speed)

            if hours_spend <= h:
                right = speed
            else:
                left = speed

        return right
    
    
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eating_time(piles, m):
            time = 0
            for pile in piles:
                time += ceil(pile / m)
            return time
          
        l = 0
        r = max(piles)
        while l < r - 1:
            m = l + (r - l) // 2
            time = eating_time(piles, m)
            if time > h:
                l = m
            else:
                r = m
        return r
        
        
            
            
