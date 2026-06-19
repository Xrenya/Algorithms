#include <iostream>
#include <vector>
#include <cassert>


class Solution {
public:
    int largestAltitude(std::vector<int>& gain) {
        int n = static_cast<int>(gain.size());
        int prev = 0;
        int max = 0;
        for (int i = 0; i < n; ++i) {
            prev += gain[i];
            max = std::max<int>(max, prev);
        }
        return max;
    }

    
    int largestAltitudeV2(std::vector<int>& gain) {
        int output = 0;
        int cur = 0;
        for (auto& val : gain) {
            cur += val;
            output = (output < cur) ? cur : output;
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

    output = sol.largestAltitudeV2(gain);
    assert((expectedOutput == output) && "Test #2 failed!");
    std::cout << "Tests are passed!" << std::endl;
    return 0;
}
