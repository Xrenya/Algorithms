#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <algorithm>
#include <cassert>


class Solution {
public:
    int minJumps(std::vector<int>& nums) {
        int n = nums.size();
        if (n <= 1) return 0;

        // 1. Precompute Smallest Prime Factor (SPF) up to 10^6
        const int MAX_VAL = 1000001;
        static std::vector<int> spf(MAX_VAL, 0);
        if (spf[2] == 0) { // Run once
            for (int i = 2; i < MAX_VAL; ++i) {
                if (spf[i] == 0) {
                    for (int j = i; j < MAX_VAL; j += i)
                        if (spf[j] == 0) spf[j] = i;
                }
            }
        }

        // 2. Map every prime to indices where nums[j] is divisible by that prime
        std::unordered_map<int, std::vector<int>> prime_to_indices;
        for (int i = 0; i < n; ++i) {
            int temp = nums[i];
            while (temp > 1) {
                int p = spf[temp];
                prime_to_indices[p].push_back(i);
                while (temp % p == 0) temp /= p;
            }
        }

        // 3. BFS for Shortest Path
        std::queue<int> q;
        std::vector<int> dist(n, -1);
        std::vector<bool> visited_prime(MAX_VAL, false);

        q.push(0);
        dist[0] = 0;

        while (!q.empty()) {
            int curr = q.front();
            q.pop();

            if (curr == n - 1) return dist[curr];

            // Option A: Adjacent Moves (+1, -1)
            for (int next_idx : {curr - 1, curr + 1}) {
                if (next_idx >= 0 && next_idx < n && dist[next_idx] == -1) {
                    dist[next_idx] = dist[curr] + 1;
                    q.push(next_idx);
                }
            }

            // Option B: Prime Teleportation
            // Rule: If nums[curr] is prime p, jump to any index j where nums[j] % p == 0
            int p = nums[curr];
            if (p >= 2 && spf[p] == p && !visited_prime[p]) {
                visited_prime[p] = true;
                for (int next_idx : prime_to_indices[p]) {
                    if (dist[next_idx] == -1) {
                        dist[next_idx] = dist[curr] + 1;
                        q.push(next_idx);
                    }
                }
            }
        }

        return -1; // Unreachable
    }
};

int main() {
  Solution sol;
  std::vector<int> nums = {2, 3, 4, 7, 9};
  int expected_output = 2;
  int output = sol.minJumps(nums);
  assert(output == expected_output && "Test #1 failed!");
  std::cout << "Tests are passed!" << std::endl;
}
