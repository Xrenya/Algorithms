#include <iostream>
#include <string>
#include <vector>
#include <cassert>

class Solution {
public:
    int rows;
    int cols;
    std::vector<std::pair<int, int>> dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

    bool dfs(int row, int col, int index, std::string& word, std::vector<std::vector<char>>& board) {
        if (index == word.size()) {
            return true;
        }
        char c = board[row][col];
        board[row][col] = '#';
        for (auto p : dirs) {
            int nrow = p.first + row;
            int ncol = p.second + col;
            if (0 <= nrow && nrow < rows && 0 <= ncol && ncol < cols && board[nrow][ncol] == word[index]) {
                if (dfs(nrow, ncol, index + 1, word, board)) {
                    return true;
                }
            }
        }
        board[row][col] = c;
        return false;
    }
    bool exist(std::vector<std::vector<char>>& board, std::string word) {
        if (board.empty() || board[0].empty()) return false;
        
        rows = board.size();
        cols = board[0].size();

        for (int row = 0; row < rows; ++row) {
            for (int col = 0; col < cols; ++col) {
                if (board[row][col] == word[0]) {
                    if (dfs(row, col, 1, word, board)) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
};

int main() {
    Solution sol;
    std::vector<std::vector<char>> board = { {'A','B','C','E'}, {'S','F','C','S'}, {'A','D','E','E'} };
    std::string word = "ABCCED";
    bool expected_output = true;
    bool output = sol.exist(board, word);
    assert ((expected_output == output) && "Test #1 failed!");
    
    std::cout << "All tests are passed!" << std::endl;

}
