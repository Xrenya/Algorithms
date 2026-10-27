#include <iostream>
#include <vector>
#include <string>

class Solution {
public:
    std::vector<std::string> createGrid(int m, int n) {
        std::string line = std::string(n - 1, '#') + '.';
        std::vector<std::string> grid(m);
        grid[0] = std::string(n, '.');
        for (int i = 1; i < m; ++i) {
            grid[i] = line;
        }
        return grid;
    }
};
