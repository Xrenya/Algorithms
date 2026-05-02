#include <iostream>
#include <vector>
#include <cassert>
#include <string>
#include <climits>

class Solution {
public:
  int minimumTotal(std::vector<std::vector<int>>& triangle) {
    int m = static_cast<int>(triangle.size());
    if (m <= 1) {
      return triangle[0][0];
    }
    int n = static_cast<int>(triangle[0].size());

    int output = INT_MAX;
    for (int i = 1; i < m; ++i) {
      n = static_cast<int>(triangle[i].size());
      for (int j = 0; j < n; ++j) {
        if (j >= 1 && j < n - 1){
          triangle[i][j] = std::min(
            triangle[i - 1][j - 1] + triangle[i][j],
            triangle[i - 1][j] + triangle[i][j]
          );
        } else if (j == 0) {
          triangle[i][j] = triangle[i - 1][j] + triangle[i][j];
        } else {
          triangle[i][j] = triangle[i - 1][j - 1] + triangle[i][j];
        }
      }
      if (i == m - 1) {
        for (int j = 0; j < n; ++j) {
          output = std::min(output, triangle[i][j]);
        }
      }
    }
    return output;  
  }
};


int main() {
  Solution sol;
  std::vector<std::vector<int>> triangle = { {2}, {3, 4}, {6, 5, 7}, {4, 1, 8, 3} };
  int expected_output = 11;
  int output = sol.minimumTotal(triangle);
  assert ((output == expected_output) && "Test #1 failed!");
  std::cout << "Tests are passed!" << std::endl;
  
  return 0;
}
