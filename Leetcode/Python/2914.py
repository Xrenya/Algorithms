class Solution:
    def minChanges(self, s: str) -> int:
        curr = s[0]
        count = 0
        min_changes = 0

        for char in s:
            if char == curr:
                count += 1
                continue

            if count % 2 == 0:
                count = 1
            else:
                count = 0
                min_changes += 1

            curr = char

        return min_changes
