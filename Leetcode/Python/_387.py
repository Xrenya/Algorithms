class Solution:
    def firstUniqChar(self, s: str) -> int:
        to_dict = defaultdict(int)
        for c in s:
            to_dict[c] += 1
            
        for i, c in enumerate(s):
            if to_dict[c] == 1:
                return i
        return -1
