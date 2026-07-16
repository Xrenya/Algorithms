class Solution {
public:
    std::vector<int> spiralOrder(std::vector<std::vector<int>>& matrix) {
        std::vector<int> output;
        int left = 0;
        int right = matrix[0].size() - 1;
        int top = 0;
        int bottom = matrix.size() - 1;
        int total = matrix.size() * matrix[0].size();
        int flag = 0;
        while (output.size() < total) {
            if (flag == 0) {
                for (int i = left; i <= right; ++i) {
                    output.push_back(matrix[top][i]);
                }
                ++top;
                flag = 1;
            } else if (flag == 1) {
                for (int i = top; i <= bottom; ++i) {
                    output.push_back(matrix[i][right]);
                }
                --right;
                flag = 2;
            } else if (flag == 2) {
                for (int i = right; i >= left; --i) {
                    output.push_back(matrix[bottom][i]);
                }
                --bottom;
                flag = 3;
            } else {
                for (int i = bottom; i >= top; --i) {
                    output.push_back(matrix[i][left]);
                }
                ++left;
                flag = 0;
            }
        }

        return output;
    }
};
