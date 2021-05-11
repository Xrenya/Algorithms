class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr = sorted(arr)
        idx = len(arr) * 0.05
        acc = arr[int(idx):len(arr)-int(idx)]
        return sum(acc) / len(acc)
