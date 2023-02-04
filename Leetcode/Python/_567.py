class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def to_dict(s):
            mapping = {}
            for char in s:
                if char not in mapping:
                    mapping[char] = 0
                mapping[char] += 1
            return mapping

        n_1 = len(s1)
        n_2 = len(s2)
        if n_1 > n_2:
            return False

        mapping_1 = to_dict(s1)
        mapping_2 = to_dict(s2[:n_1])
        if mapping_1 == mapping_2:
            return True
        left = 0
        for right in range(n_1, n_2):
            remove_char = s2[left]
            left += 1
            add_char = s2[right]
            mapping_2[remove_char] -= 1
            if mapping_2[remove_char] == 0:
                del mapping_2[remove_char]
            if add_char not in mapping_2:
                mapping_2[add_char] = 0
            mapping_2[add_char] += 1
            if mapping_1 == mapping_2:
                return True
        return False

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
