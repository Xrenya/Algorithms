class Solution {
private:
    vector<vector<int>> dirs {{1, 0}, {0, 1}, {-1, 0}, {0, -1}, {1, 1}, {-1, -1}, {-1, 1}, {1, -1}};

public:
    int getNeighbours(vector<vector<int>>& board, int row, int col, int maxRows, int maxCols) {
        int alive = 0;
        for (int i = 0; i < dirs.size(); ++i) {
            int newRow = row + dirs[i][0];
            int newCol = col + dirs[i][1];
            if (newRow >= 0 && newRow < maxRows && newCol >= 0 && newCol < maxCols) {
                alive += board[newRow][newCol];
            }
        }
        return alive;
    }
    void gameOfLife(vector<vector<int>>& board) {
        std::set<pair<int, int>> alive, dead;
        int maxRows = board.size();
        int maxCols = board[0].size();
        for (int i = 0; i < maxRows; ++i) {
            for (int j = 0; j < maxCols; ++j) {
                int nei = getNeighbours(board, i, j, maxRows, maxCols);
                if (board[i][j] == 0 && nei == 3) {
                    alive.insert({i, j});
                } else if (board[i][j] && (nei > 3 || nei < 2)) {
                    dead.insert({i, j});
                }
            }
        }

        for (int i = 0; i < maxRows; ++i) {
            for (int j = 0; j < maxCols; ++j) {
                std::pair<int, int> cell = {i, j};
                if (dead.contains(cell)) {
                    board[i][j] = 0;
                } else if (alive.contains(cell)) {
                    board[i][j] = 1;
                }
            }
        }
    }
};
