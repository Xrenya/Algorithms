class Solution:
    def reverseWords(self, s: str) -> str:
        array = s.split(" ")
        outArray = []
        for word in array:
            string = ''
            for letter in word[::-1]:
                string += letter
            outArray.append(string)
        return ' '.join(outArray)

