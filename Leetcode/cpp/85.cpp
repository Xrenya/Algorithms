#include <iostream>
#include <algorithm>
#include <vector>


class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        int rows = matrix.size();
        if (rows == 0) return 0;
        int cols = matrix[0].size();
        int max_area = 0;
        std::vector<std::vector<int>> dp(rows, std::vector<int>(cols, 0));
        for (int row = 0; row < rows; ++row) {
            for (int col = 0; col < cols; ++col) {
                if (matrix[row][col] == '1') {
                    dp[row][col] = col == 0 ? 1 : dp[row][col - 1] + 1;
                    int width = dp[row][col];
                    for (int k = row; k >= 0; --k) {
                        width = std::min(width, dp[k][col]);
                        max_area = std::max(max_area, width * (row - k + 1));
                    }
                }
            }
        }
        return max_area;
    }
};
