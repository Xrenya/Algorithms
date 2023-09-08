class Solution:
    def findOrder(self, numCourses, prerequisites):
        WHITE = 1
        GRAY = 2
        BLACK = 3
        adj = defaultdict(list)

        for dest, src in prerequisites:
            adj[src].append(dest)

        ordered = []
        self.is_possible = True

        # All vertices are white at the start
        color = {k: WHITE for k in range(numCourses)}
        def dfs(node):
            if not self.is_possible:
                return

            color[node] = GRAY

            if node in adj:
                for neighbor in adj[node]:
                    if color[neighbor] == WHITE:
                        dfs(neighbor)
                    elif color[neighbor] == GRAY:
                         # An edge to a GRAY vertex represents a cycle
                        self.is_possible = False

            color[node] = BLACK
            ordered.append(node)

        for vertex in range(numCourses):
            # If the node is unprocessed, then call dfs on it.
            if color[vertex] == WHITE:
                dfs(vertex)

        return ordered[::-1] if self.is_possible else []
        

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        
        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])
            indegree[prerequisite[0]] += 1
            
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
                
                
        visited = 0
        while queue:
            node = queue.popleft()
            visited += 1
            
            for next_node in adj[node]:
                indegree[next_node] -= 1
                if indegree[next_node] == 0:
                    queue.append(next_node)
                    
        return visited == numCourses
                    
