class Solution:
    # Brute force
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        out = num_people * [0]
        give = 0
        while candies > 0:
            out[give % num_people] += min(candies, give + 1)
            give += 1
            candies -= give
        return out
