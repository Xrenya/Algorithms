#include <iostream>
#include <string>
#include <cassert>

class Solution {
public:
    int furthestDistanceFromOrigin(std::string moves) {
        int left = 0, right = 0, any = 0;
        for (auto move : moves) {
            if (move == 'L') {
                ++left;
            } else if (move == 'R') {
                ++right;
            } else {
                ++any;
            }
        }
        return std::abs(left - right) + any;
    }
};

int main(void) {
    Solution sol;
    std::string input = "L_RL__R";
    int expected_output = 3;
    int output = sol.furthestDistanceFromOrigin(input);
    assert ((expected_output == output) &&  "Test is not passed!");   
    std::cout << "Tests are passed!" << std::endl;
    return 0;
}
