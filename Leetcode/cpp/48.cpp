#include <iostream>
#include <vector>
#include <cassert>

class Solution {
public:
  void rotate(std::vector<std::vector<int>>& matrix) {
    int m = static_cast<int>(matrix.size());
    int n = static_cast<int>(matrix[0].size());
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j <= i; ++j) {
        std::swap(matrix[j][i], matrix[i][j]);  
      }
    }

    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n / 2; ++j) {
        std::swap(matrix[i][j], matrix[i][n - 1 - j]);  
      }
    }

  }
};

int main() {
    Solution sol;
    std::vector<std::vector<int>> input = { {1, 2, 3}, {4, 5, 6}, {7, 8, 9} };
    std::vector<std::vector<int>> expected_output = {{7, 4, 1}, {8, 5, 2}, {9, 6, 3} };
    sol.rotate(input);
    assert(input == expected_output && "Test #1 failed!");
    std::cout << "Tests are passed!" << std::endl;
}
