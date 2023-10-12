class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        lenght = mountain_arr.length()
        
        l, r = 1, lenght - 2
        
        while l != r:
            idx = l + (r - l) // 2
            if mountain_arr.get(idx) < mountain_arr.get(idx + 1):
                l = idx + 1
            else:
                r = idx
                
        peak_idx = l
        
        l = 0
        r = peak_idx
        while l != r:
            idx = l + (r - l) // 2
            if mountain_arr.get(idx) < target:
                l = idx + 1
            else:
                r = idx
        if mountain_arr.get(l) == target:
            return l
        
        l = peak_idx + 1
        r = lenght - 1
        while l != r:
            idx = l + (r - l) // 2
            if mountain_arr.get(idx) > target:
                l = idx + 1
            else:
                r = idx
                
        if mountain_arr.get(l) == target:
            return l
        
        return -1
