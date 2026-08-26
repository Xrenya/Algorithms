class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        output = s
        cur = ""
        left = 0
        found = False
        for right in range(len(s)):
            if s[right] == "1":
                k -= 1
            cur = s[left:right + 1]
            if k == 0 and len(output) > len(cur):
                output = cur
                found = True
            elif k == 0 and len(output) == len(cur):
                output = output if output < cur else cur
                found = True
            while k <= 0:
                if s[left] == "1":
                    k += 1
                left += 1
                cur = s[left:right + 1]
                if k == 0 and len(output) > len(cur):
                    output = cur
                elif k == 0 and len(output) == len(cur):
                    output = output if output < cur else cur

        return output if found else ""
