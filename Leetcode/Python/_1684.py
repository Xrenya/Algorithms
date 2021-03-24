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
 
class Solution(object):
    def countConsistentStrings(self, allowed, words):
        counter = 0
        hashMap = {}
        
        for letter in allowed:
            if letter not in hashMap:
                hashMap[letter] = 1
                
        for word in words:
            consistent = 1
            for letter in word:
                if letter not in hashMap:
                    consistent = 0
                    
            if consistent == 1:
                counter += 1
                
        return counter
 
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        counter = len(words)
        hashMap = dict()
        for letter in allowed:
            if letter not in hashMap:
                hashMap[letter] = 1 
        
        for word in words:
            for letter in word:
                if not letter in hashMap:
                    counter -= 1
                    break
        return counter
