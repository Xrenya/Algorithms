from typing import (
    List,
)

class Solution:
    """
    @param array: An array.
    @return: An interger.
    """
    def findNumber(self, array: List[int]) -> int:
        # Write your code here.
        votes = {}
        maximum = float("inf")
        output = 0
        for num in array:
            if num not in votes:
                votes[num] = 0
            votes[num] += 1
            if votes[num] > output:
                output = votes[num]
                maximum = num
            elif votes[num] == output:
                if num < maximum:
                    maximum = num
        return maximum
