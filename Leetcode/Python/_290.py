class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hash_map = {}
        reverse_map = {}
        splited = s.split(" ")
        if len(pattern) != len(splited):
            return False
        for pat, match in zip(pattern, splited):
            if pat not in hash_map:
                hash_map[pat] = match
            if match not in reverse_map:
                reverse_map[match] = pat
            if pat != reverse_map[match] or hash_map[pat] != match:
                return False
        return True
