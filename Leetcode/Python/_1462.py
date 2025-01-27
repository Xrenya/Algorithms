class Solution:
    def isPrerequisite(self, adj_list, visited, src, target):
        visited[src] = True
        if src == target:
            return True

        for adj in adj_list.get(src, []):
            if not visited[adj]:
                if self.isPrerequisite(adj_list, visited, adj, target):
                    return True
        return False
        
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj_list = {i: [] for i in range(numCourses)}

        for edge in prerequisites:
            adj_list[edge[0]].append(edge[1])

        output = []

        for query in queries:
            visited = [False] * numCourses
            output.append(self.isPrerequisite(adj_list, visited, query[0], query[1]))

        return output
