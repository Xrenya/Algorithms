class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        heap = [(-nums[0], 0)]
        max_seq_sum = nums[0]
        
        for i in range(1, len(nums)):
            while i - heap[0][1] > k:
                heapq.heappop(heap)
            cur = max(0, -heap[0][0]) + nums[i]
            max_seq_sum = max(max_seq_sum, cur)
            heapq.heappush(heap, (-cur, i))
        return max_seq_sum
