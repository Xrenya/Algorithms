class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        output = [0] * n

        bleft, mleft = 0, 0
        bright, mright = 0, 0
        
        for i in range(n):
            output[i] += mleft
            bleft += int(boxes[i])
            mleft += bleft

            j = n - i - 1
            output[j] += mright
            bright += int(boxes[j])
            mright += bright

        return output
