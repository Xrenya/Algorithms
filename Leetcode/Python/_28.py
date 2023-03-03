class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0 and len(haystack) == 0:
            return 0
        window = len(needle)
        for i in range(len(haystack) + 1 - window):
            if haystack[i:i + window] == needle:
                return i
        return -1
      
      
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1

        mapping_needle = {}
        mapping = {}
        for char in needle:
            if char not in mapping_needle:
                mapping_needle[char] = 0
            mapping_needle[char] += 1

        for i in range(len(needle)):
            char = haystack[i]
            if char not in mapping:
                mapping[char] = 0
            mapping[char] += 1

        if mapping_needle == mapping and haystack[:len(needle)] == needle:
            return 0
        left = 0
        for right in range(len(needle), len(haystack)):
            remove_char = haystack[left]
            mapping[remove_char] -= 1
            if mapping[remove_char] == 0:
                del mapping[remove_char]

            add_char = haystack[right]
            if add_char not in mapping:
                mapping[add_char] = 0
            mapping[add_char] += 1
            left += 1

            if mapping == mapping_needle and haystack[left:right + 1] == needle:
                return left
        return -1
