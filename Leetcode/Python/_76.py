class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        dict_t = Counter(t)
        required = len(dict_t)

        l, r = 0, 0

        formed = 0

        ans = float("inf"), None, None
        window_counts = {}
        while r < len(s):
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1

            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1
            while l <= r and formed == required:
                char = s[l]

                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                window_counts[char] -= 1
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1

                l += 1
            r += 1
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]
        

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
