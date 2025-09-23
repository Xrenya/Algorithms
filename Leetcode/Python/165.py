class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        nums1 = version1.split(".")
        nums2 = version2.split(".")
        n1, n2 = len(nums1), len(nums2)
        
        for i in range(max(n1, n2)):
            d1 = int(nums1[i]) if i < n1 else 0
            d2 = int(nums2[i]) if i < n2 else 0
            if d1 != d2:
                return 1 if d1 > d2 else -1
            
        return 0
        
    def compareVersion_v1(self, version1: str, version2: str) -> int:
        idx_v1 = 0
        idx_v2 = 0
        version1 = version1.split(".")
        version2 = version2.split(".")
        while idx_v1 < len(version1) and idx_v2 < len(version2):
            v1 = int(version1[idx_v1])
            v2 = int(version2[idx_v2])
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
            idx_v1 += 1
            idx_v2 += 1
        
        while idx_v1 < len(version1):
            v1 = int(version1[idx_v1])
            if v1 > 0:
                return 1
            idx_v1 += 1 
        
        while idx_v2 < len(version2):
            v2 = int(version2[idx_v2])
            if v2 > 0:
                return -1
            idx_v2 += 1
        
        return 0
