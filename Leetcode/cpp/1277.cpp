class Solution {
public:
    int countSquares(vector<vector<int>>& matrix) {
        int ROWS = matrix.size(), COLS = matrix[0].size();
        if (ROWS == 0) return 0;
        if (COLS == 0) return 0;
        int size = (ROWS + 1) * (COLS + 1);
        vector<int> dp(size, 0);
        int count = 0;
        for (int row = 0; row < ROWS; ++row) {
            for (int col = 0; col < COLS; ++col) {
                if (matrix[row][col]) {
                    int cr = row + 1;
                    int cc = col + 1;
                    dp[cr * (COLS + 1) + cc] = std::min(
                        dp[cr * (COLS + 1) + (cc - 1)],
                        std::min(
                            dp[(cr - 1) * (COLS + 1) + cc],
                            dp[(cr - 1) * (COLS + 1) + (cc - 1)]
                        )
                    ) + 1;
                    count += dp[cr * (COLS + 1) + cc];
                }
            }
        }
        return count;
    }
};
