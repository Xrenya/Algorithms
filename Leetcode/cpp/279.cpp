#include <iostream>
#include <set>
#include <cassert>
#include <cmath>

class Solution {
    std::set<int> squares;

public:
    bool isDivisiable(int n, int count) {
        if (count == 1) {
            return squares.contains(n);
        }

        for (auto square : squares) {
            if (isDivisiable(n - square, count - 1)) {
                return true;
            }
        }
        return false;
    }
    int numSquares(int n) {
        squares.clear();
        for (int i = 1; i < (int) std::sqrt(n) + 1; ++i) {
            squares.insert(i * i);
        }
        for (int i = 1; i <= n; ++i) {
            if (isDivisiable(n, i)) {
                return i;
            }
        }
        return -1;
    }
};

int main() {
    Solution sol;
    int n = 12;
    int exepectedOutput = 3;
    int otuput = sol.numSquares(n);
    
    assert((exepectedOutput == otuput) && "Test #1 failed!");
    std::cout << "Tests are passed!" << std::endl;
    return 0;
}
