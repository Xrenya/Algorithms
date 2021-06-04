class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = [-stone for stone in stones]
        heapq.heapify(q)
        while (len(q)) > 1:
            heapq.heappush(q, heapq.heappop(q) - heapq.heappop(q))
        return -q[0]
    
    
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones)
        while len(stones) > 1:
            last = stones.pop()
            previous = stones.pop()
            if last != previous:
                diff = last - previous
                stones = [diff] + stones
            stones = sorted(stones)
        if len(stones) == 1:
            return stones[0]
        if len(stones) == 0:
            return 0
        return diff
    
