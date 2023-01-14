class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        adj = [[] for _ in range(ord("z") - ord("a") + 1)]
        for i in range(len(s1)):
            adj[ord(s1[i]) - ord('a')].append(ord(s2[i]) - ord('a'))
            adj[ord(s2[i]) - ord('a')].append(ord(s1[i]) - ord('a'))
    
        def dfs(node, visited, minimum):
            if minimum > node:
                minimum = node
            visited.add(node)
            for child in adj[node]:
                if child in visited:
                    continue
                minimum = dfs(child, visited, minimum)
            return minimum

        output = ''
        for char in baseStr:
            output += chr(dfs(ord(char) - ord('a'), set(), float("inf")) + ord('a'))
            
        return output
