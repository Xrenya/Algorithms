class Solution:
    def minInsertions(self, s: str) -> int:
        length = len(s)
        insert = left = index = 0

        while index < length:
            if s[index] == "(":
                left += 1
                index += 1
            else:
                if left > 0:
                    left -= 1
                else:
                    insert += 1
                if index < length - 1 and s[index + 1] == ")":
                    index += 2
                else:
                    insert += 1
                    index += 1
        insert += left * 2
        return insert
