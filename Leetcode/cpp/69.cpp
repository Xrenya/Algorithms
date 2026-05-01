#include <iostream>
#include <vector>
#include <cassert>
#include <algorithm>

class Solution {
public:
    int mySqrt(int x) {
        if (x < 2) {
            return x;
        }

        int left = 2, right = x / 2;
        while (left <= right) {
            long long mid = left + (right - left) / 2;
            if (mid * mid == x) {
                return mid;
            } else if (mid * mid < x) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return right;
    }
};
int main() {
    Solution sol;
	int input = 8;
	int expected_output = 2;
	
	int output = sol.mySqrt(input);
	assert (expected_output == output && "Test #1 failed!");
	std::cout << "Tests are passed!" << std::endl;

}
