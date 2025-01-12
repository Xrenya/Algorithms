class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        l = len(s)

        if l % 2 == 1:
            return False

        opened = []
        unlocked = []

        for i in range(l):
            if locked[i] == "0":
                unlocked.append(i)
            elif s[i] == "(":
                opened.append(i)
            elif s[i] == ")":
                if opened:
                    opened.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False
        while opened and unlocked and opened[-1] < unlocked[-1]:
            opened.pop()
            unlocked.pop()

        if opened:
            return False
        
        return True
