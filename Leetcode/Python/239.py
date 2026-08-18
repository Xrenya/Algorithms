class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque([])
        output = []
        for i in range(k):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)

        output.append(nums[q[0]])
        for i in range(k, len(nums)):
            if q and q[0] + k == i:
                q.popleft()

            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            output.append(nums[q[0]])

        return output
