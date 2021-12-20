class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needed_chars = dict()
        for c in t:
            needed_chars[c] = needed_chars.get(c, 0) + 1

        different_char_needed = len(needed_chars)
        
        ans_left, ans_right = -1, len(s)
        
        left = 0
        
        for right, c in enumerate(s):
            if c not in needed_chars:
                continue
            needed_chars[c] -= 1
            if needed_chars[c] == 0:
                different_char_needed -= 1
                if different_char_needed == 0:
                    while different_char_needed == 0:
                        c = s[left]
                        left += 1
                        if c not in needed_chars:
                            continue
                        needed_chars[c] += 1
                        if needed_chars[c] == 1:
                            different_char_needed += 1
                    if right - left + 2 < ans_right - ans_left:
                        ans_left = left - 1
                        ans_right = right + 1
        
        if ans_left == -1:
            return ""
        return s[ans_left:ans_right]
