#include <iostream>
#include <vector>
#include <cassert>   // assert
#include <numeric>   // std::accumulate

class Solution {
public:
    bool canPartitionGrid(std::vector<std::vector<int>>& grid) {
        long long target = 0;
        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[0].size(); ++j) {
                target += grid[i][j];
            }
        }
        if (target % 2 != 0) return false;
        target /= 2;

        long long cur = 0;
        for (int i = 0; i < grid.size(); ++i) {
            cur += std::accumulate(grid[i].begin(), grid[i].end(), 0LL);
            if (cur == target) return true;
            if (cur > target) break;
        }

        cur = 0;
        for (int j = 0; j < grid[0].size(); ++j) {
            for (int i = 0; i < grid.size(); ++i) {
                cur += grid[i][j];
            }
            if (cur == target) return true;
            if (cur > target) break;
        }
        return false;
    }
};

int main() {
    // 1. Create an instance of the Solution class
    Solution sol;

    // 2. Define test cases (grids)
    // Test 1: Valid (Horizontal cut after row 0: 1+1 = 2, Total=4)
    std::vector<std::vector<int>> grid1 = {{1, 1}, {1, 1}};
    
    // Test 2: Invalid (Total=10, target=5, no cut works)
    std::vector<std::vector<int>> grid2 = {{1, 2}, {3, 4}};

    // Test 3: Valid (Vertical cut after col 0: 1+3 = 4, Total=8)
    std::vector<std::vector<int>> grid3 = {{1, 2}, {3, 2}};

    assert(sol.canPartitionGrid(grid1) == true);
    assert(sol.canPartitionGrid(grid2) == false);
    assert(sol.canPartitionGrid(grid3) == true);

    std::cout << "All tests passed!" << std::endl;

    return 0;
}
