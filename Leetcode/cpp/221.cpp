#include <iostream>
#include <vector>
#include <cassert>

class Solution {
public:
  int maximalSquare(std::vector<std::vector<char>>& matrix) {
    int m = static_cast<int>(matrix.size());
    int n = static_cast<int>(matrix[0].size());
    int max_square = 0;
    std::vector<std::vector<int>> dp(m, std::vector<int>(n, 0));
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
          if (matrix[i][j] == '1' && (j == 0 || i == 0)) {
              dp[i][j] = 1;
          } else if (matrix[i][j] == '1') {
              dp[i][j] = std::min<int>(
                  dp[i][j - 1], 
                  std::min<int>(dp[i - 1][j - 1], dp[i - 1][j])
              ) + 1;
          }
          max_square = std::max<int>(dp[i][j], max_square);
        }
    }
    return max_square * max_square;
  }
};

int main() {
    Solution sol;
    std::vector<std::vector<char>> input = {{'1', '0', '1', '0', '0'},
                                            {'1', '0', '1', '1', '1'},
                                            {'1', '1', '1', '1', '1'},
                                            {'1', '0', '0', '1', '0'}
                                           };
    int expected_output = 4;
    int output = sol.maximalSquare(input);
    assert(output == expected_output && "Test #1 failed!");
    std::cout << "Tests are passed!" << std::endl;
}
