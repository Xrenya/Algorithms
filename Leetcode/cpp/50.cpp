#include <iostream>
#include <vector>
#include <cassert>
#include <algorithm>

class Solution {
public:
    double binaryExp(double x, long long n) {
        if (n == 0) {
            return 1;
        } else if (n == 1) {
            return x;
        }

        if (n < 0) {
            return 1.0 / binaryExp(x, -1 * n);
        }
        else if (n % 2 == 0) {
            return binaryExp(x * x, n / 2);
        }
        return x * binaryExp(x * x, (n - 1) / 2);
    }
    double myPow(double x, int n) {
        return binaryExp(x, (long long) n);
    }
};

int main() {
    Solution sol;
	int n = 10;
	double x = 2;
	double expected_output = 1024.0;
	
	double output = sol.myPow(x, n);
	assert (expected_output == output && "Test #1 failed!");
	std::cout << "Tests are passed!" << std::endl;

}
