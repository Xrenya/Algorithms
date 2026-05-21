class Trie:
    def __init__(self, val = -1):
        self.val = val
        self.map = {}

    def __repr__(self):
        return f"Trie({self.val}, {self.map})"


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie()

        for num in arr1:
            tmp = []
            cur = trie
            while num:
                tmp.append(num % 10)
                num //= 10
            for i in range(len(tmp) - 1, -1, -1):
                digit = tmp[i]
                if digit not in cur.map:
                    cur.map[digit] = Trie(digit)
                cur = cur.map[digit]

        output: int = 0
        for num in arr2:
            tmp = []
            cur = trie
            while num:
                tmp.append(num % 10)
                num //= 10 
            length = 0
            for i in range(len(tmp) - 1, -1, -1):
                digit = tmp[i]
                if digit not in cur.map:
                    break
                cur = cur.map[digit]
                length += 1
            output = max(output, length)
        return output 
