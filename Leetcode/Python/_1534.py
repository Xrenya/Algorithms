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
