class SummaryRanges:

    def __init__(self):
        self.array = []

    def addNum(self, value: int) -> None:
        left = 0
        right = len(self.array) - 1
        while left <= right:
            m = left + (right - left) // 2
            e = self.array[m]
            if e[0] <= value <= e[1]:
                return
            elif e[1] < value:
                left = m + 1
            else:
                right = m - 1
        index = left
        self.array.insert(index, [value, value])
        if index < len(self.array) - 1 and self.array[index + 1][0] == value + 1:
            self.array[index][1] = self.array[index + 1][1]
            del self.array[index + 1]
        if index - 1 >= 0 and self.array[index - 1][1] == value - 1:
            self.array[index - 1][1] = self.array[index][1]
            del self.array[index]
            
    def getIntervals(self) -> List[List[int]]:
        return self.array    
    

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
