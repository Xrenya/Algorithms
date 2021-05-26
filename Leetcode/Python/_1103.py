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

class Solution:
    def distributeCandies(self, c: int, n: int) -> List[int]:
        k = math.floor((math.sqrt(1+8*c)-1)/2/n)
        res = [0 for i in range(n)]
        for i in range(n):
            res[i] = (i+1+(k-1)*(n)+i+1)*k/2
        remain = c - sum(res)
        i = 0
        cur = k*n+1
        while remain >= 0:
            res[i] += min(remain,cur)
            remain -= cur
            
            cur += 1
            i += 1
        return [int(i) for i in res]
