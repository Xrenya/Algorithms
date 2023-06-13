class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = {}

class Trie:
    def __init__(self):
        self.trie = TrieNode()

    def insert(self, array):
        my_trie = self.trie
        for a in array:
            if a not in my_trie.children:
                my_trie.children[a] = TrieNode()
            my_trie = my_trie.children[a] 
        my_trie.count += 1

    def search(self, array):
        my_trie = self.trie
        for a in array:
            if a in my_trie.children:
                my_trie = my_trie.children[a]
            else:
                return 0
        return my_trie.count

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        my_trie = Trie()
        count = 0
        n = len(grid)
        
        for row in grid:
            my_trie.insert(row)
        
        for c in range(n):
            col_array = [grid[i][c] for i in range(n)]
            count += my_trie.search(col_array)
    
        return count    
    
class Solution:
    def eq(self, grid, row_index, col_index):
        for i in range(len(grid)):
            if grid[row_index][i] != grid[i][col_index]:
                return 0
        return 1

    def equalPairs(self, grid: List[List[int]]) -> int:
        mapping = defaultdict(list)
        for index, val in enumerate(grid):
            mapping[val[0]].append(index)
        count = 0
        for i in range(len(grid)):
            if grid[0][i] in mapping:
                for row_index in mapping[grid[0][i]]:
                    count += self.eq(grid, row_index, i)
        return count
