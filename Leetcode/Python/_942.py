class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        array = []
        l = 0
        r = len(s)
        for letter in s:
            if letter == "I":
                array.append(l)
            else:
                array.append(r)
            l = l + (letter == "I")
            r = r - (letter == "D")
        array.append(l)
        return array
                
