class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        firstList.sort(key=lambda x: (x[0], -x[1]))
        secondList.sort(key=lambda x: (x[0], -x[1]))
        idx_1, idx_2 = 0, 0
        output = []
        while idx_1 < len(firstList) and idx_2 < len(secondList):
            lo = max(firstList[idx_1][0], secondList[idx_2][0])
            hi = min(firstList[idx_1][1], secondList[idx_2][1])

            if lo <= hi:
                output.append([lo, hi])

            if firstList[idx_1][1] < secondList[idx_2][1]:
                idx_1 += 1
            else:
                idx_2 += 1

        return output
