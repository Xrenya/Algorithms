class Solution:
    def minimumLength(self, s: str) -> int:
        char_freq = Counter(s)

        delete = 0
        for f in char_freq.values():
            if f % 2 == 1:
                delete += f - 1
            else:
                delete += f - 2
        return len(s) - delete
