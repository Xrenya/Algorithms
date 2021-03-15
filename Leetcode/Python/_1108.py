class Solution:
    def defangIPaddr(self, address: str) -> str:
        addr = str()
        # Iterate over the string and replace '.' with '[.]'
        # Time complexity O(n)
        for string in address:
            if string == '.':
                addr += '[.]'
            else:
                addr += string
        return addr
