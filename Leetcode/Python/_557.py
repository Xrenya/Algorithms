class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(word):
            if not word:
                return ""
            return word[-1] + reverse(word[:-1])

        return " ".join([reverse(x) for x in s.split()])


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

