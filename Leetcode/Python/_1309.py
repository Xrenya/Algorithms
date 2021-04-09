class Solution:
    def freqAlphabets(self, s: str) -> str:
        string = ""
        idx = 0
        
        while idx < len(s):
            if idx < len(s) - 2:
                if s[idx+2] == "#":
                    string += chr(96+int(s[idx:idx+2]))
                    idx += 3
                else:
                    string += chr(96+int(s[idx]))
                    idx += 1
            else:
                string += chr(96+int(s[idx]))
                idx += 1
        return string
                
