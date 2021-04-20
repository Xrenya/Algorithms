class Solution:
    def islandPerimeter(self, g: List[List[int]]) -> int:
        count = 0
        for x in range(len(g)):
            for y in range(len(g[0])):
                if not g[x][y]:
                    continue
        
                count += 4
                                
                if y and g[x][y - 1]:
                    count -= 2
                if x and g[x - 1][y]:
                    count -= 2
        return count
