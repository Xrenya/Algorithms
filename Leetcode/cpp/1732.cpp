#include <iostream>
#include <vector>
#include <cassert>
#include <climits>

class Solution {
public:
    int largestAltitude(std::vector<int>& gain) {
        int output = 0;
        int cur = 0;
        for (auto& val : gain) {
            cur += val;
            output = output < cur ? cur : output;
        }
        return output;
    }
};

int main() {
    Solution sol;
    std::vector<int> gain = {-5, 1, 5, 0, -7};
    int expectedOutput = 1;
    int output = sol.largestAltitude(gain);
    
    assert((expectedOutput == output) && "Test #1 failed!");
    
    std::cout << "All tests are passed!" << std::endl;
    
    return 0;
}
