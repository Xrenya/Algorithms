#include <iostream>
#include <vector>
#include <cassert>
#include <string>
#include <climits>

class Solution {
public:
  int minPathSum(std::vector<std::vector<int>>& grid) {
    int m = static_cast<int>(grid.size());
    int n = static_cast<int>(grid[0].size());

    for (int i = 1; i < m; ++i) {
      grid[i][0] += grid[i - 1][0];
    }
    
    for (int j = 1; j < n; ++j) {
      grid[0][j] += grid[0][j - 1];
    }

    for (int i = 1; i < m; ++i) {
      for (int j = 1; j < n; ++j) {
        grid[i][j] += std::min(grid[i - 1][j], grid[i][j - 1]);
      }
    }
    // debug:
    // for (int i = 0; i < m; ++i) {
    //   for (int j = 0; j < n; ++j) {
    //     std::cout << grid[i][j] << " ";
    //   }
    //   std::cout << std::endl;
    // }
    return grid[m - 1][n - 1];
  }
};

int main() {
  Solution sol;
  std::vector<std::vector<int>> grid = { {1, 3, 1}, {1, 5, 1}, {4, 2, 1} };
  int expected_output = 7;
  int output = sol.minPathSum(grid);
  assert ((output == expected_output) && "Test #1 failed!");
  std::cout << "Tests are passed!" << std::endl;
  
  return 0;
}


/*
class Solution {
public:
    // 2-D solution without extra space: O(1)
    int minPathSum(vector<vector<int>>& grid) {
      int COLS = grid[0].size(), ROWS = grid.size();
      for (int row = 1; row < ROWS; row++) {
        grid[row][0] += grid[row - 1][0];
      }

      for (int col = 1; col < COLS; col++) {
        grid[0][col] += grid[0][col - 1];
      }

      for (int row = 1; row < ROWS; row++) {
        for (int col = 1; col < COLS; col++) {
          grid[row][col] = min(grid[row][col] + grid[row][col - 1], grid[row][col] + grid[row - 1][col]);
        }
      }
      //Print matrix 
      // for (int row = 0; row < ROWS; row++) {
      //   for (int col = 0; col < COLS; col++) {
      //     std::cout << grid[row][col] << " ";
      //   } 
      //   std::cout << std::endl;
      // }
      return grid[ROWS - 1][COLS - 1];
    }
};

class Solution {
public:
    // 1-D solution
    int minPathSum(vector<vector<int>>& grid) {
      int COLS = grid[0].size(), ROWS = grid.size();
      vector<int> mat(COLS, 0);
      mat[0] = grid[0][0];
      // Fill the first row
      for (int col = 1; col < COLS; col++) {
        mat[col] = grid[0][col] + mat[col - 1];
      }
      for (int row = 1; row < ROWS; row++) {
        for (int col = 0; col < COLS; col++) {
          if (col == 0) {
            mat[0] += grid[row][col];
          } else {
            mat[col] = min(
              grid[row][col] + mat[col - 1], grid[row][col] + mat[col]
            );
          }
        } 
      }

      // for (int col = 0; col < COLS; col++) {
      //   std::cout << mat[col] << " ";
      // }
      return mat[COLS - 1];
    }
};

class Solution {
public:
    // 2-D solution
    int minPathSum(vector<vector<int>>& grid) {
      int COLS = grid[0].size(), ROWS = grid.size();
      vector<vector<int>> mat(ROWS, vector<int>(COLS, -1));
      mat[0][0] = grid[0][0];
      // Fill the first row
      for (int col = 1; col < COLS; col++) {
        mat[0][col] = grid[0][col] + mat[0][col - 1];
      }
      // Fill the first col
      for (int row = 1; row < ROWS; row++) {
        mat[row][0] = grid[row][0] + mat[row - 1][0];
      } 
      // Fill the rest of the matrix
      for (int row = 1; row < ROWS; row++) {
        for (int col = 1; col < COLS; col++) {
          mat[row][col] = min(
            grid[row][col] + mat[row][col - 1], grid[row][col] + mat[row - 1][col]
          );
        } 
      }
      // Print matrix 
      // for (int row = 0; row < ROWS; row++) {
      //   for (int col = 0; col < COLS; col++) {
      //     std::cout << mat[row][col] << " ";
      //   } 
      //   std::cout << std::endl;
      // }
      return mat[ROWS - 1][COLS - 1];
    }
};
*/
