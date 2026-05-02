#include <iostream>
#include <vector>
#include <cassert>
#include <string>
#include <climits>

class Solution {
public:
  int uniquePathsWithObstacles(std::vector<std::vector<int>>& obstacleGrid) {
    int m = static_cast<int>(obstacleGrid.size());
    int n = static_cast<int>(obstacleGrid[0].size());

    if (obstacleGrid[m - 1][n - 1] || obstacleGrid[0][0]) return 0;

    std::vector<std::vector<int>> dp(m, std::vector<int>(n, 10001));
    for (int i = 0; i < m; ++i) {
      if (obstacleGrid[i][0]) {
        break;
      }
      dp[i][0] = 1;
    }
    
    for (int j = 1; j < n; ++j) {
      if (obstacleGrid[0][j]) {
        break;
      }
      dp[0][j] = 1;
    }

    for (int i = 1; i < m; ++i) {
      for (int j = 1; j < n; ++j) {
        if (obstacleGrid[i][j]) {
          continue;
        }
        int above = dp[i][j - 1] != 10001 ? dp[i][j - 1] : 0;
        int prev = dp[i - 1][j] != 10001 ? dp[i - 1][j] : 0;
        dp[i][j] = above + prev;
      }
    }
  // for (int i = 0; i < m; ++i) {
  //   for (int j = 0; j < n; ++j) {
  //     std::cout << dp[i][j] << " ";
  //   }
  //   std::cout << std::endl;
  // }
  return dp[m - 1][n - 1] != 10001 ? dp[m - 1][n - 1] : 0;
  }
};

int main() {
  Solution sol;
  std::vector<std::vector<int>> grid = { {0, 0, 0}, {0, 1, 0}, {0, 0, 0} };
  int expected_output = 2;
  int output = sol.uniquePathsWithObstacles(grid);
  assert ((output == expected_output) && "Test #1 failed!");
  std::cout << "Tests are passed!" << std::endl;
  
  return 0;
}
