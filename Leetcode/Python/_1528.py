class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # Time complexity O(n)
        array = [0] * len(indices)
        for idx in range(len(indices)):
            array[indices[idx]] = s[idx]
            
        return "".join(array)
      
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        HashMap = {}
        string = str()
        for idx in range(len(indices)):
            HashMap[indices[idx]] = s[idx]
        for idx in range(len(indices)):
            string += HashMap[idx]
        return string
