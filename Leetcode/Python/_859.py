class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        def mapping(s):
            m = {}
            for char in s:
                if char not in m:
                    m[char] = 0
                m[char] += 1
            return m

        if len(s) != len(goal):
            return False

        if s == goal:
            m = mapping(s)
            for k, v in m.items():
                if v > 1:
                    return True
            return False

        first_idx = second_idx = -1
        for i in range(len(s)):
            if s[i] != goal[i]:
                if first_idx == -1:
                    first_idx = i
                elif second_idx == -1:
                    second_idx = i
                else:
                    return False

        return s[first_idx] == goal[second_idx] and s[second_idx] == goal[first_idx]
