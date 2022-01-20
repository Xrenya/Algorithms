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
        
        
            
            
