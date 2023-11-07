class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arr = []
        for i in range(len(dist)):
            arr.append(dist[i] / speed[i])
        
        arr.sort()
        output = 0
        for i in range(len(arr)):
            if arr[i] <= i:
                break
            output += 1
            
        return output
