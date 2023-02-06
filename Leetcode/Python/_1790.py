class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        cnt = 0
        output = []
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                output.append((c1, c2))
                cnt += 1
        print(output)
        return False if cnt > 2 else True if cnt == 2 and output[0][0] == output[1][1] and output[0][1] == output[1][0] else False
