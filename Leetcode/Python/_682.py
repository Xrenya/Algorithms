class Solution:
    def calPoints(self, ops: List[str]) -> int:
        array = []
        for op in ops:
            if op == 'C':
                array.pop()
            elif op == 'D':
                array.append(array[-1]*2)
            elif op == "+":
                array.append(array[-1] + array[-2])
            else:
                array.append(int(op))
        return sum(array)
