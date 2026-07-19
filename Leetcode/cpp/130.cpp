class Solution {
public:
    void solve(vector<vector<char>>& board) {
        int ROWS = board.size();
        int COLS = board[0].size();
        std::vector<std::vector<int>> dirs = { {1, 0}, {0, 1}, {0, -1}, {-1, 0} };

        std::function<void(int, int)> dfs = [&](int row, int col) -> void {
            board[row][col] = 'V';
            for (int i = 0; i < dirs.size(); ++i) {
                int new_row = row + dirs[i][0];
                int new_col = col + dirs[i][1];
                if (new_row >= 0 && new_row < ROWS && new_col >= 0 && new_col < COLS && board[new_row][new_col] == 'O') {
                    dfs(new_row, new_col);
                }
            }
        };

        std::cout << std::endl;
        for (int i = 0; i < ROWS; ++i) {
            for (int j = 0; j < COLS; ++j) {
                if (((i == 0 || i == ROWS - 1) || (j == 0 || j == COLS - 1)) && board[i][j] == 'O') {
                    dfs(i, j);
                }
            }
        }

        for (int i = 0; i < ROWS; ++i) {
            for (int j = 0; j < COLS; ++j) {
                if (board[i][j] == 'V') {
                    board[i][j] = 'O';
                } else if (board[i][j] == 'O') {
                    board[i][j] = 'X';
                }
            }
        }
    }
};
