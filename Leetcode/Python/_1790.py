class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        s1_frequency_map = [0] * 26
        s2_frequency_map = [0] * 26
        num_diffs = 0

        for i in range(len(s1)):
            s1_char = s1[i]
            s2_char = s2[i]

            if s1_char != s2_char:
                num_diffs += 1
                if num_diffs > 2:
                    return False

            s1_frequency_map[ord(s1_char) - ord("a")] += 1
            s2_frequency_map[ord(s2_char) - ord("a")] += 1

        return s1_frequency_map == s2_frequency_map


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
