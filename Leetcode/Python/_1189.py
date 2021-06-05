class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b = text.count('b')
        a = text.count('a')
        l = int(text.count('l') / 2)
        o = int(text.count('o') / 2)
        n = text.count('n')
        f = [b, a, l, o, n]
        return min(f)
      
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashMap = collections.Counter(text)
        b = hashMap.get('b', 0)
        a = hashMap.get('a', 0)
        l = int(hashMap.get('l', 0)/2)
        o = int(hashMap.get('o', 0)/2)
        n = hashMap.get('n', 0)
        f = [b, a, l, o, n]
        return min(f)
      
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashMap = {"b": 1, "a": 1, 
                   "l": 2, "o": 2, "n": 1}
        currentMap = {}
        for letter in text:
            currentMap[letter] = currentMap.get(letter, 0) + 1
        count = inf
        for key in hashMap.keys():
            count = min(count, currentMap.get(key, 0) // hashMap[key])
        return count
