#include <iostream>
#include <vector>
#include <cassert>
#include <algorithm>

class Solution {
public:
    int minimumEffort(std::vector<std::vector<int>>& tasks) {
        std::sort(tasks.begin(), tasks.end(), [&](std::vector<int>& a, std::vector<int>& b) {
            return a[1] - a[0] < b[1] - b[0];
        });
        int ans = 0;
        for (auto task : tasks) {
            ans = std::max<int>(ans + task[0], task[1]);
        }
        return ans;
    }
};

int main() {
    Solution sol;
    std::vector<std::vector<int>> tasks = {{1, 2}, {2, 4}, {4, 8}};
    int expected_output = 8;
    
    int output = sol.minimumEffort(tasks);
    assert ((expected_output == output) && "Test #1 failed!");
    std::cout << "Tests are passed!" << std::endl;
    return 0;
}
