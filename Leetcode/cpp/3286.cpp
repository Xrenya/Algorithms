class Solution {
public:
    bool findSafeWalk(std::vector<std::vector<int>>& grid, int health) {
        int rows = grid.size();
        int cols = grid[0].size();
        std::vector<std::vector<int>> dp(rows, std::vector<int>(cols, -1));
        std::deque<std::vector<int>> dq;
        
        if (grid[0][0]) {
            --health;
        }
        if (health <= 0) return false;
        dq.push_back({0, 0, health});

        std::vector<std::pair<int, int>> mov = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    
        while (!dq.empty()) {
            std::vector<int> current = std::move(dq.front()); 
            int crow = current[0];
            int ccol = current[1];
            int chealth = current[2];
            dq.pop_front();

            dp[crow][ccol] = std::max<int>(dp[crow][ccol], chealth);

            for (auto [nrow, ncol] : mov) {
                int next_row = crow + nrow;
                int next_col = ccol + ncol;

                if (crow == rows - 1 && ccol == cols - 1 && chealth >= 1) {
                    return true;
                }

                if (chealth < dp[crow][ccol]) {
                    continue;
                }

                if (next_col >=0 && next_col < cols && next_row >= 0 && next_row < rows && (grid[next_row][next_col] == 0 || (grid[next_row][next_col] == 1 && chealth > 0))) {
                    if (grid[next_row][next_col] == 0 && chealth > dp[next_row][next_col]) {
                        dp[next_row][next_col] = chealth;
                        dq.push_back({next_row, next_col, chealth});
                    } else if (chealth - 1 > dp[next_row][next_col]) {
                        dp[next_row][next_col] = chealth - 1;
                        dq.push_back({next_row, next_col, chealth - 1});
                    }
                } 
            }
        }
        return dp[rows - 1][cols - 1] >= 1 ? true : false;

    }
};
