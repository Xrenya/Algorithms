class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("(al)", "al").replace("()", "o")
        
 class Solution:
    def interpret(self, command: str) -> str:
        string = str()
        for idx, c in enumerate(command):
            if c == 'G':
                string += c
            elif c == '(':
                if command[idx+1] == ')':
                    string += 'o'
                elif command[idx+1] == 'a':
                    string += 'al'
                else:
                    pass
            else:
                pass
        return string
