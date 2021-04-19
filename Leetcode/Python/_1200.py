class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        array = []
        minimum = +inf
        for i in range(1, len(arr)):
            if abs(arr[i]-arr[i-1]) < minimum:
                minimum = abs(arr[i]-arr[i-1])
                array = [[arr[i-1], arr[i]]]
            elif abs(arr[i]-arr[i-1]) == minimum:
                array.append([arr[i-1], arr[i]])
        return array
                
