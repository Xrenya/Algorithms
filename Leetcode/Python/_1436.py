class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        graph = defaultdict(list)
        for a, b in paths:
            graph[a].append(b)
            if b not in graph:
                graph[b] = []

        for k, v in graph.items():
            if not len(v):
                return k
                

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        res=[]
        for item in paths:
            res.append(item[0])
        for item in paths:
            if item[1] not in res:
                return(item[1])
