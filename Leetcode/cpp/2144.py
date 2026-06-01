#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>

class Solution {
public:
    int minimumCost(std::vector<int>& cost) {
        std::sort(cost.begin(), cost.end());
        int output = 0;
        int bought = 0;
        for (int i = cost.size() - 1; i >= 0; --i) {
            ++bought;
            output += cost[i];
            if (bought == 3) {
                output -= cost[i];
                bought = 0;
            }
        }
        return output;
    }
};
int main() {
    Solution sol;
    std::vector<int> cost = {1, 2, 3};
    int exepectedOutput = 5;
    int outpt = sol.minimumCost(cost);
    assert((exepectedOutput == outpt) && "Test #1 failed!");
    std::cout << "Tests are passed!" << std::endl;
    return 0;
}
