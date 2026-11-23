class ProductOfNumbers:

    def __init__(self):
        self.dq = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.dq = [1]
        else:
            self.dq.append(self.dq[-1] * num)

    def getProduct(self, k: int) -> int:
        if k > len(self.dq) - 1:
            return 0
        return self.dq[-1] // self.dq[-k - 1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
