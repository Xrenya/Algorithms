class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        visited = set()
        q = deque([(0, 0)])
        forbidden = set(forbidden)
        furthest = max(x, max(forbidden)) + a + b
        
        res = 0
        while q:
            n = len(q)
            for _ in range(n):
                p, is_back = q.popleft()
                if p in forbidden or (p, is_back) in visited or p < 0 or p > furthest:
                    continue
                if p == x:
                    return res 
                visited.add((p, is_back))
                q.append((p + a, 0))
                if not is_back:
                    q.append((p - b, 1))
                
            res += 1
        return -1
