class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        hashMap = {}
        for letter in chars:
            if letter not in hashMap:
                hashMap[letter] = 1
            else:
                hashMap[letter] += 1
        acc = 0
        for word in words:
            temp = hashMap.copy()
            string = ''
            for letter in word:
                if letter not in hashMap:
                    break
                else:
                    if temp[letter] > 0:
                        string += letter
                        temp[letter] -= 1
                    else:
                        break
            if string == word:
                acc += len(word)
        return acc
          
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        hashMap = collections.Counter(chars)
        acc = 0
        for word in words:
            temp = hashMap.copy()
            string = ''
            for letter in word:
                if letter not in hashMap:
                    break
                else:
                    if temp[letter] > 0:
                        string += letter
                        temp[letter] -= 1
                    else:
                        break
            if string == word:
                acc += len(word)
        return acc
