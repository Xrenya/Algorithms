#include <iostream>
#include <vector>
#include <cassert>
#include <algorithm>

class Solution {
public:
    int trailingZeroes(int n) {
        int countZeros = 0;
        long long currentMultiple = 5;
        while (n >= currentMultiple) {
            countZeros += (n / currentMultiple);
            currentMultiple *= 5;
        }
        return countZeros;
    }
};

int main() {
    Solution sol;
	int input = 5;
	int expected_output = 1;
	
	int output = sol.trailingZeroes(input);
	assert (expected_output == output && "Test #1 failed!");
	std::cout << "Tests are passed!" << std::endl;

}
