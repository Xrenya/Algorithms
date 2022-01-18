class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        for i in range(len(flowerbed)):
            prev = 0 if i == 0 else flowerbed[i - 1]
            following = 0 if i == len(flowerbed) - 1 else flowerbed[i + 1]
            if flowerbed[i] == 0 and prev == 0 and following == 0:
                cnt += 1
                flowerbed[i] = 1
        return cnt >= n
