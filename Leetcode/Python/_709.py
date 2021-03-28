class Solution:
    def toLowerCase(self, str: str) -> str:
        string = ""
        for idx in range(len(str)):
            if str[idx].isupper():
                string += str[idx].lower()
            else:
                string += str[idx]
        return string
            
class Solution:
    def toLowerCase(self, str: str) -> str:
        return "".join(chr(ord(c) + 32) if 65 <= ord(c) <= 90 else c for c in str)
            
class Solution:
    def toLowerCase(self, str):
        string = ""
        for char in str:
            if ord(char) >= 65 and ord(char) <= 90:
                string += chr(ord(char)+32)
            else:
                string += char
        
        return string
      
