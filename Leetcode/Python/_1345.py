class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0

        graph = {}
        for i in range(n):
            node = arr[i]
            if node not in graph:
                graph[node] = []
            
            graph[node].append(i)

        cur_nodes = [0]
        visited = {0,}
        step = 0

        while cur_nodes:
            next_nodes = []

            for node in cur_nodes:
                if node == n - 1:
                    return step

                for child in graph[arr[node]]:
                    if child not in visited:
                        visited.add(child)
                        next_nodes.append(child)

                graph[arr[node]].clear()

                for child in [node - 1, node + 1]:
                    if 0 <= child < n and child not in visited:
                        visited.add(child)
                        next_nodes.append(child)

            cur_nodes = next_nodes
            step += 1

        return -1
