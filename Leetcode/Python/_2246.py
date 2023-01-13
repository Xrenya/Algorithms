class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        def dfs(node):
            longest = second_longest = 0

            for child in adj[node]:
                path_len = dfs(child)
                if s[child] != s[node]:  # parten and child have different values
                    if path_len > longest:
                        second_longest = longest
                        longest = path_len
                    elif path_len > second_longest:
                        second_longest = path_len

            self.ans = max(self.ans, longest + second_longest + 1)  # largest path including parent with at most two children 
            return longest + 1  # largest path including parent


        self.ans = 1
        adj = defaultdict(list)
        for i, root in enumerate(parent[1:], start=1):
            adj[root].append(i)
        print(adj)
        dfs(0)
        return self.ans
