class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        output = 0
        last = None
        for num in timeSeries:
            if output:
                if last >= num:
                    output += num + duration - last - 1
                else:
                    output += duration
                last = num + duration - 1
            else:
                last = num + duration - 1
                output = duration
        return output

      
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        output = []
        for num in timeSeries:
            if output:
                if output[-1] >= num:
                    output += [i for i in range(output[-1] + 1, num+duration, 1)]
                else:
                    output += [i for i in range(num, num+duration, 1)]
            else:
                output += [i for i in range(num, num+duration, 1)]   
        return len(output)
