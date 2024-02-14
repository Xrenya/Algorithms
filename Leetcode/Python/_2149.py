class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos_idx = neg_idx = 0
        output = [0] * len(nums)
        for n in nums:
            if n < 0:
                output[neg_idx] = n
                neg_idx += 2
            else:
                output[pos_idx] = n
                pos_idx += 2
        return output


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = deque()
        neg = deque()
        output = []
        for n in nums:
            if n < 0:
                neg.append(n)
            else:
                pos.append(n)
        while neg and pos:
            output.append(pos.popleft())
            output.append(neg.popleft())
        return output
