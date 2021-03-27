class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        # Brute force solution
        counter = 0
        lenght = len(arr)
        for i in range(lenght-2):
            for j in range(lenght-1):
                for k in range(lenght):
                    if i<j and j<k and k<lenght:
                        if abs(arr[i]-arr[j])<=a and abs(arr[j]-arr[k])<=b and abs(arr[i]-arr[k])<=c:
                            print(arr[i], arr[j], arr[k])
                            counter += 1
                        else:
                            pass
        return counter
    
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        
        size = len(arr)
        counter = 0
        
        for i in range(size-2):
            for j in range(i+1, size-1):
                for k in range(j+1, size):
                    
                    ok_a = abs(arr[i] - arr[j]) <= a
                    ok_b = abs(arr[j] - arr[k]) <= b
                    ok_c = abs(arr[i] - arr[k]) <= c
                    
                    if all((ok_a, ok_b, ok_c)):
                        counter += 1   
        return counter
