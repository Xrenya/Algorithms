class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left, max_len = 0, 0
        mapping = {}
        for right in range(len(s)):
            if s[right] not in mapping:
                mapping[s[right]] = 0
            mapping[s[right]] += 1
            while len(mapping) > 2:
                mapping[s[left]] -= 1
                if mapping[s[left]] == 0:
                    mapping.pop(s[left])
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len
