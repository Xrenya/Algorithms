#include <iostream>
#include <vector>
#include <cassert>


class Solution {
public:
    std::vector<std::vector<char>> rotateTheBox(std::vector<std::vector<char>>& boxGrid) {
        int m = static_cast<int>(boxGrid.size());
        int n = static_cast<int>(boxGrid[0].size());
        std::vector<std::vector<char>> output(n, std::vector<char>(m, '\0'));

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                output[j][m - 1 - i] = boxGrid[i][j];
            }
        }

        for (int j = 0; j < m; ++j) {
            int empty = n - 1;
            for (int i = n - 1; i >= 0; --i) {
                if (output[i][j] == '*') {
                    empty = i - 1;
                } else if (output[i][j] == '#') {
                    output[empty][j] = output[i][j];
                    if (empty != i) {
                        output[i][j] = '.';
                    }
                    --empty;
                }
            }
        }
        // for (int i = n - 1; i >= 0; --i) {
        //   std::reverse(output[i].begin(), output[i].end());
        // }

        return output;
    }
};


int main() {
	std::vector<std::vector<char>> boxGrid = { {'#', '.', '*', '.'}, {'#', '#', '*', '.'} };
	std::vector<std::vector<char>> expected_output = {{'#', '.'},
                                             {'#', '#'},
                                             {'*', '*'},
                                             {'.', '.'}};
    Solution sol;
    std::vector<std::vector<char>> output = sol.rotateTheBox(boxGrid);
    
    assert (output == expected_output && "Test #1 failed!");
    
    std::cout << "All tests are passed!" << std::endl;
    
    return 0;
}
