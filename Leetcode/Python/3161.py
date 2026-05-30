class Solution:
    def __init__(self,):
        self.seg = []
        self.st = SortedList()
        self.mx = 50000

    def update(self, index: int, val: int, p: int, l: int, r: int) -> None:
        if l == r:
            self.seg[p] = val
            return
        mid = l + (r - l) // 2
        if index <= mid:
            self.update(index, val, p * 2, l, mid)
        else:
            self.update(index, val, p * 2 | 1, mid + 1, r)
        
        self.seg[p] = max(self.seg[p * 2], self.seg[p * 2 | 1])

    def query(self, L: int, R: int, p: int, l: int, r: int) -> int:
        if L <= l and r <= R:
            return self.seg[p]
        mid = l + (r - l) // 2
        output = 0
        if L <= mid:
            output = max(output, self.query(L, R, p * 2, l, mid))
        if R > mid:
            output = max(output, self.query(L, R, p * 2 | 1, mid + 1, r))
        return output

    def getResults(self, queries: List[List[int]]) -> List[bool]:
        self.seg = [0] * (self.mx * 4)
        self.st = SortedList([0, self.mx])
        self.update(self.mx, self.mx, 1, 0, self.mx)
        output = []

        for q in queries:
            if q[0] == 1:
                x = q[1]
                index = min(len(self.st) - 1, self.st.bisect_right(x))

                r = self.st[index]
                l = self.st[index - 1] if index > 0 else self.st[0]
                self.update(x, x- l, 1, 0, self.mx)
                self.update(r, r - x, 1, 0, self.mx)
                self.st.add(x)
            else:
                x, sz = q[1], q[2]
                index = min(len(self.st) - 1, self.st.bisect_right(x))
                pre = self.st[0] if index == 0 else self.st[index - 1]

                max_space = max(x - pre, self.query(0, pre, 1, 0, self.mx))
                output.append(max_space >= sz)
            
        return output
