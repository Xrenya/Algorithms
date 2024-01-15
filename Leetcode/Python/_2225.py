class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        graph = {}
        for w, l in matches:
            if w not in graph:
                graph[w] = [0, 0]
            if l not in graph:
                graph[l] = [0, 0]
            graph[w][0] += 1
            graph[l][1] += 1
            
        
        ones = []
        zeros = []
        for p, (w, l) in graph.items():
            if l == 0 and w >= 1:
                zeros.append(p)
            elif l == 1:
                ones.append(p)
        return [sorted(zeros), sorted(ones)]
