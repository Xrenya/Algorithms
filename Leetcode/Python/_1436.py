class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        res=[]
        for item in paths:
            res.append(item[0])
        for item in paths:
            if item[1] not in res:
                return(item[1])
