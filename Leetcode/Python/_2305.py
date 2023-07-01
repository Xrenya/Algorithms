class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        dist = [0] * k
        n = len(cookies)

        def backtrack(index, count):
            if n - index < count:
                return float("inf")

            if index == n:
                return max(dist)

            ans = float("inf")
            for j in range(k):
                count -= int(dist[j] == 0)
                dist[j] += cookies[index]
                ans = min(ans, backtrack(index + 1, count))
                dist[j] -= cookies[index]
                count += int(dist[j] == 0)

            return ans

        return backtrack(0, k)
