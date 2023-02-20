class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:

        unionList = list(range(len(edges) + 1))

        def find(x):
            if x == unionList[x]:
                return x
            return find(unionList[x])

        def union(x, y):
            if find(x) != find(y):
                unionList[x] = y

            # check and saving the last edge in loop

        loop = None

        # check parent
        parent = {}
        for i, j in edges:
            parent.setdefault(j, []).append(i)
            if find(i) == find(j):
                loop = [i, j]
            union(i, j)

        # get the node which has more than one parent
        doubleParent = [i for i in parent if len(parent[i]) > 1]
        hasDoubleParent = len(doubleParent)

        # which situation we are? 
        if not hasDoubleParent and loop:
            return loop
        # simple,return the edge in loop
        elif hasDoubleParent and not loop:
            return [parent[doubleParent[0]][1], doubleParent[0]]
            # easy, return the edge between node with second parent
        else:
        # get first edge and second edge(one of them should be removed)
            firstEdge = [parent[doubleParent[0]][0], doubleParent[0]]
    
            secondEdge = [parent[doubleParent[0]][1], doubleParent[0]]
        
            # remove second edge and check there is a loop or not
            deleteSecondEdge = edges[:]
            deleteSecondEdge.remove(secondEdge)
            unionList = list(range(len(edges) + 1))
        
            for i, j in deleteSecondEdge:
                if find(i) == find(j):
                    # opps,there is still a loop, we should remove first edge, so return it 
                    return firstEdge
                union(i, j)
            # seems like remove second edge works.
            return secondEdge
