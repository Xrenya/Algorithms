class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Time complexity O(2n)
        # Find the maximum in the array
        maximum = 0
        for candy in candies:
            if candy > maximum:
                maximum = candy
        arr = []
        # If the new value is higher than the maximum append True, else it is False
        for candy in candies:
            if (candy + extraCandies) >= maximum:
                arr.append(True)
            else:
                arr.append(False)
        return arr
