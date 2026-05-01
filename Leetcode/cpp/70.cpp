#include <iostream>
#include <vector>
#include <cassert>
#include <algorithm>
#include <unordered_map>
#include <functional> // Required for std::hash

class Solution {
public:
    int climbStairs(int n) {
        int last = 1, prev = 2;
        if (n == 1) {
            return 1;
        } else if (n == 2) {
            return 2;
        }
        for (int i = 3; i <= n; ++i) {
            int tmp = prev + last;
            last = prev;
            prev = tmp;
        }
        return prev;
    }
};

/*
// Recursive without optimization
class Solution {
public:
    int recusive(int step, int steps) {
        if (step > steps) {
            return 0;
        }
        if (step == steps) {
            return 1;
        }
        return recusive(step + 1, steps) + recusive(step + 2, steps);
    } 
    int climbStairs(int n) { return recusive(0, n); }

// Recursive with optimization
class Solution {
public:
    int recusive(int step, int steps, std::vector<int>& memo) {
        if (step > steps) {
            return 0;
        }
        if (step == steps) {
            return 1;
        }
        if (memo[step] > 0) {
            return memo[step];
        }
        memo[step] = recusive(step + 1, steps, memo) + recusive(step + 2, steps, memo);
        return memo[step];
    } 
    int climbStairs(int n) {
        std::vector<int> memo(n + 1, 0);
        return recusive(0, n, memo);
    }
};

*/
int main() {
    Solution sol;
	int input = 3;
	int expected_output = 3;
	
	double output = sol.climbStairs(input);
	assert (expected_output == output && "Test #1 failed!");
	std::cout << "Tests are passed!" << std::endl;

}
