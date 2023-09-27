class Solution(object):
    def decodeAtIndex(self, s, k):
        size = 0
        for c in s:
            if c.isdigit():
                size *= int(c)
            else:
                size += 1

        for i in range(len(s) - 1, -1, -1):
            c = s[i]
            k %= size
            if k == 0 and c.isalpha():
                return c
            if c.isdigit():
                size /= int(c)
            else:
                size -= 1
        return ""
