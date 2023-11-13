class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "AEIOUaeiou"
        count = {char: 0 for char in vowels}
        for char in s:
            if char in vowels:
                count[char] += 1
        index = 0
        output = ""
        for char in s:
            if char not in vowels:
                output += char
            else:
                while count[vowels[index]] == 0:
                    index += 1
                output += vowels[index]
                count[vowels[index]] -= 1
        return output
