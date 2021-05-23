class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for log in logs:
            if log == "./":
                continue
            elif log == "../":
                count -= 1
                if count < 0:
                    count = 0
            else:
                count += 1
        return count
        
