#include <iostream>
#include <vector>
#include <cassert>


class Solution {
public:
    bool areSimilar(std::vector<std::vector<int>>& mat, int k) {
        int rows = mat.size();
        int cols = mat[0].size();
        k %= cols;
        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                if (mat[i][(j + k) % cols] != mat[i][j]) {
                    return false;
                }
            }
        }
        return true;
    }
};

int main() {
	// your code goes here
	Solution sol;
	std::vector<std::vector<int>> mat = { {1,2,3}, {4,5,6}, {7,8,9} };
	bool output = sol.areSimilar(mat, 3);
	assert (output == 1 && "Output is incorrect!\n");
	
	output = sol.areSimilar(mat, 2);
	assert (output == 0 && "Output is incorrect!\n");
    std::cout << "All tests are passed!" << std::endl;
}
