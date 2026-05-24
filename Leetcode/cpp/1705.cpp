#include <iostream>
#include <vector>
#include <queue>
#include <cassert>
#include <algorithm>

class Solution {
public:
    int eatenApples(std::vector<int>& apples, std::vector<int>& days) {
        using PairType = std::pair<int, int>;
        std::priority_queue<PairType, std::vector<PairType>, std::greater<PairType>> pq;
        int eaten_apples = 0;
        int currentDay = 0;
        int totalDays = days.size();
        while (currentDay < totalDays || !pq.empty()) {
            if (currentDay < totalDays && apples[currentDay] > 0) {
                int expirationDay = currentDay + days[currentDay] - 1;
                pq.emplace(expirationDay, apples[currentDay]);
            }
            
            while (!pq.empty() && pq.top().first < currentDay) {
                pq.pop();
            }
            
            if (!pq.empty()) {
                auto [expirationDay, appleCount] = pq.top();
                pq.pop();
                ++eaten_apples;
                --appleCount;
                if (appleCount > 0 && expirationDay > currentDay) {
                    pq.emplace(expirationDay, appleCount);
                }
            }
            ++currentDay;
        }
        return eaten_apples;
    }
};


int main() {
    Solution sol;
    std::vector<int> apples = {1, 2, 3, 5, 2};
    std::vector<int> days = {3, 2, 1, 4, 2};
    int expectedOutput = 7;
    
    int output = sol.eatenApples(apples, days);
    
    assert((expectedOutput == output) && "Test #1 failed!");
    
    std::cout << "Tests are passed!" << std::endl;
    
    return 0;
}
