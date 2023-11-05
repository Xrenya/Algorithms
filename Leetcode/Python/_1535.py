class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        max_el = max(arr)
        cur = arr[0]
        queue = deque(arr[1:])
        streak = 0
        while queue:
            opp = queue.popleft()
            if opp < cur:
                queue.append(opp)
                streak += 1
            else:
                queue.append(cur)
                cur = opp
                streak = 1
            if streak == k or cur == max_el:
                return cur
