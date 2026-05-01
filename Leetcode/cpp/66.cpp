#include <iostream>
#include <vector>
#include <cassert>
#include <algorithm>

class Solution {
public:
    std::vector<int> plusOne(std::vector<int>& digits) {
        std::vector<int> output;
        int carry = 0;
        for (int i = digits.size() - 1; i >= 0; --i) {
            if (i == digits.size() - 1) {
                carry += digits[i] + 1;
            } else {
                carry += digits[i];
            }
            output.push_back(carry % 10);
            carry /= 10;
        }
        if (carry) {
            output.push_back(carry);
        }
        std::reverse(output.begin(), output.end());
        return output;
    }
};

int main() {
    Solution sol;
	std::vector<int> input = {1, 2, 3};
	std::vector<int> expected_output = {1, 2, 4};
	
	std::vector<int> output = sol.plusOne(input);
	assert (expected_output == output && "Test #1 failed!");
	std::cout << "Tests are passed!" << std::endl;

}
