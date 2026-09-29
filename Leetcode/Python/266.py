class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        mapping = {}
        for char in s:
            mapping[char] = mapping.get(char, 0) + 1
        odd_count = 0
        for count in mapping.values():
            if count % 2 == 1:
                odd_count += 1
        return odd_count == 1 if len(s) % 2 == 1 else odd_count == 0
