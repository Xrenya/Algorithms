#include <iostream>
#include <vector>
#include <queue>

class Solution {
public:
    long long bfs(int row, int col, std::vector<std::vector<int>>& grid, std::vector<std::pair<int, int>>& dirs, const int& ROWS, const int& COLS) {
        long long cur = grid[row][col];
        grid[row][col] = 0;
        std::queue<std::pair<int, int>> stack;
        stack.push(std::pair<int, int> {row, col});
        while (!stack.empty()) {
            std::pair<int, int> p = stack.front();
            stack.pop();
            for (auto d : dirs) {
                long long new_row = p.first + d.first;
                int new_col = p.second + d.second;
                if (new_row >= 0 && new_row < ROWS && new_col >= 0 && new_col < COLS && grid[new_row][new_col] != 0) {
                    cur += grid[new_row][new_col];
                    grid[new_row][new_col] = 0;
                    stack.push(std::pair<int, int> {new_row, new_col});
                }
            }
        }
        return cur;
    }

    int countIslands(std::vector<std::vector<int>>& grid, int k) {
        int ROWS = grid.size();
        int COLS = grid[0].size();
        int count = 0;
        std::vector<std::pair<int, int>> dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        for (int i = 0; i < ROWS; ++i) {
            for (int j = 0; j < COLS; ++j) {
                if (grid[i][j] != 0) {
                    long long output = bfs(i, j, grid, dirs, ROWS, COLS);
                    if (output % k == 0) {
                        ++count;
                    }
                }
            }
        }
        return count;
    }
};
