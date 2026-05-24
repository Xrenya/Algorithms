#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>

class Solution {
    std::vector<int> dp;
public:
    void dfs(std::vector<int>& arr, int index, const int& d, const int& n) {
        if (dp[index] != 1) {
            return;
        }
        for (int i = index - 1; i >= 0 && index - i <= d && arr[i] < arr[index]; --i) {
            dfs(arr, i, d, n);
            dp[index] = std::max<int>(dp[index], dp[i] + 1);
        }
        for (int i = index + 1; i < n && i - index <= d && arr[i] < arr[index]; ++i) {
            dfs(arr, i, d, n);
            dp[index] = std::max<int>(dp[index], dp[i] + 1);
        }

    }

    int maxJumps(std::vector<int>& arr, int d) {
        int n = static_cast<int>(arr.size());
        dp.resize(n, 1);
        for (int i = 0; i < n; ++i) {
            dfs(arr, i, d, n);
        }
        return *std::max_element(dp.begin(), dp.end());
    }
};


int main() {
    Solution sol;
    std::vector<int> arr{6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12};
    int d = 2;
    int exepected_output = 4;
    int output = sol.maxJumps(arr, d);
    
    assert((exepected_output == output) && "Test #1 failed!");
    std::cout << "Tests are passed!" << std::endl;
    return 0;
}
