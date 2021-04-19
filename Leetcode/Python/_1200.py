class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort() # O(nlogn)
        history, min_diff = {}, float("inf")
        
        for i in range(len(arr)-1): # O(n)
            if min_diff >= abs(arr[i] - arr[i+1]):
                min_diff = abs(arr[i] - arr[i+1])
                if min_diff not in history:
                    history[min_diff] = []
                    history[min_diff].append([arr[i], arr[i+1]])
                else:
                    history[min_diff].append([arr[i], arr[i+1]])
      
        return history[min_diff]

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
                
