class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        output = []
        target = len(graph) - 1
        lst = []
        def backtrack(node):
            lst.append(node)
            if node == target:
                output.append(lst[:])
                return
            for cur_node in graph[node]:
                backtrack(cur_node)
                lst.pop()
            return

        backtrack(0)
        return output
