class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        std::set<std::pair<char, int>> rows, cols;
        std::set<std::pair<char, std::pair<int, int>>> section;
        for (int i = 0; i < board.size(); ++i) {
            for (int j = 0; j < board[0].size(); ++j) {
                if (board[i][j] != '.') {
                    std::pair<char, int> addRows = {board[i][j], i};
                    std::pair<char, int> addCols = {board[i][j], j};
                    std::pair<int, int> sec = {i / 3, j / 3};
                    std::pair<char, std::pair<int, int> > addSection = {board[i][j], sec};
                    if (rows.contains(addRows) || cols.contains(addCols) || section.contains(addSection)) {
                        return false;
                    }
                    rows.insert(addRows);
                    cols.insert(addCols);
                    section.insert(addSection);
                }
            }
        }
        return true;
    }
};
