class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def to_dict(s):
            hash_map = {}
            for c in s:
                if c not in hash_map:
                    hash_map[c] = 0
                hash_map[c] += 1        
            return hash_map
        
        hash_map = to_dict(s1)
        for i in range(0, len(s2) - len(s1) + 1):
            if to_dict(s2[i:i + len(s1)]) == hash_map:
                return True
        return False
