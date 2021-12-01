class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        dist = float("inf")
        out = None
        for s in letters:
            diff = abs(ord(target) - ord(s))
            if diff < dist and ord(target) < ord(s) :
                dist = diff
                out = s
        if out is None:
            return letters[0]
        return out
