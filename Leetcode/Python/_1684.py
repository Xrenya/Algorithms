class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # Brute force solution 
        counter = 0
        inc = 0
        for string in words:
            for s in string:
                if s in allowed:
                    inc += 1
                else:
                    inc -= 1
            if inc == len(string):
                counter += 1
            inc = 0
        return counter
            
