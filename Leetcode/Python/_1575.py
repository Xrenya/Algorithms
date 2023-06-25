class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)

        memo = {}

        def solve(cur_city, remaining_fuel):
            if remaining_fuel < 0:
                return 0
            if (cur_city, remaining_fuel) in memo:
                return memo[(cur_city, remaining_fuel)]

            ans = 0
            if cur_city == finish:
                ans = 1
            for next_city in range(n):
                if next_city != cur_city:
                    ans = (ans + solve(
                        next_city, remaining_fuel -
                        abs(locations[cur_city] - locations[next_city]))) % 1000000007

            memo[(cur_city, remaining_fuel)] = ans
            return ans

        return solve(start, fuel)
