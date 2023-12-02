class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        def to_mapping(s):
            d = {}
            for char in s:
                if char not in d:
                    d[char] = 0
                d[char] += 1
            return d

        chars = to_mapping(chars)
        output = 0
        for word in words:
            w = to_mapping(word)
            add = True
            for k, v in w.items():
                if k not in chars or v > chars[k]:
                    add = False
                    break

            if add:
                output += len(word)
        return output



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
