class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        output = [0, 0]
        dist = float("inf")
        for w in range(1, area + 1):
            if area % w == 0:
                l = area // w
                if w > l:
                    break
                if dist > l - w:
                     dist = l - w
                output = [l, w]
        return output
