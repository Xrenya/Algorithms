class SmallestInfiniteSet:

    def __init__(self):
        self.cur_num = 1
        self.nums = []
        self._exists = set()

    def popSmallest(self) -> int:
        if self.nums:
            ans = heapq.heappop(self.nums)
            self._exists.remove(ans)
            return ans
        ans = self.cur_num
        self.cur_num += 1
        return ans

    def addBack(self, num: int) -> None:
        if num >= self.cur_num or num in self._exists:
            return
        self._exists.add(num)
        heapq.heappush(self.nums, num)
