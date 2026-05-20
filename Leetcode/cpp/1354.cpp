#include <iostream>
#include <vector>
#include <cassert>
#include <queue>
#include <numeric>

class Solution {
public:
    bool isPossible(std::vector<int>& target) {
        if (target.size() == 1) {
            return target[0] == 1;
        }

        // 1. Prevent overflow by using long long
        long long total = std::accumulate(target.begin(), target.end(), 0LL);
        auto maxHeap = [](int a, int b) {
            return a < b;
        };
        std::priority_queue<int, std::vector<int>, decltype(maxHeap)> pq(maxHeap);
        for (auto num : target) {
            pq.push(num);
        }
        // C++ priority_queue is a max-heap by default
        // std::priority_queue<int> pq(target.begin(), target.end());

        while (pq.top() > 1) {
            long long largest = pq.top();
            pq.pop();
            
            long long remainder = total - largest;

            // 2. If the rest of the elements sum to 1, it's always possible (e.g., [1, 10])
            if (remainder == 1) {
                return true;
            }

            // 3. Invalid cases: remainder is 0, or largest is smaller than the rest
            if (remainder == 0 || largest <= remainder) {
                return false;
            }

            // 4. Use modulo to fast-forward the subtractions
            long long x = largest % remainder;

            // 5. If it divides perfectly, we hit 0 instead of 1, which is invalid
            if (x == 0) {
                return false;
            }

            pq.push(x);
            total = remainder + x;
        }
        return true;

    }
};

int main() {
    Solution sol;
    std::vector<int> target = {1, 1, 1, 2};
    bool expected_output = false;
    bool output = sol.isPossible(target);
    assert(output == expected_output && "Test #1 failed!");


    std::cout << "Tests are passed!\n";
    return 0;
}
