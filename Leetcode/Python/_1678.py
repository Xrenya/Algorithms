class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("(al)", "al").replace("()", "o")
        
class Solution:
    def interpret(self, command: str) -> str:
        string = str()
        for idx, char in enumerate(command):
            if char == 'G':
                string += char
            elif char == '(':
                if command[idx+1] == ')':
                    string += 'o'
                elif command[idx+1] == 'a':
                    string += 'al'
                else:
                    pass
            else:
                pass
        return string
   
class Solution:
    def interpret(self, command: str) -> str:
        string = str()
        for idx, char in enumerate(command):
            if char == 'G':
                string += char
            elif char == '(' and command[idx+1] == ')':
                string += 'o'
            elif char == '(' and command[idx+1] == 'a':
                string += 'al'
            else:
                pass
        return string
