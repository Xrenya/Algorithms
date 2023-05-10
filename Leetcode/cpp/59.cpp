class Solution {
public:
  vector<vector<int>> generateMatrix(int n) {
    std::vector<std::vector<int>> mat(n, std::vector<int>(n));
    int val = 1, dir = 0, left = 0, right = n, top = 0, bottom = n, N = n * n;
    while (val <= N) {
      if (dir == 0) {
        for (int i = left; i < right; i++) {
          mat[top][i] = val;
          val++;
        }
        top++;
        dir = 1;
      } else if (dir == 1) {
        for (int i = top; i < bottom; i++) {
          mat[i][right - 1] = val;
          val++;
        }
        right--;
        dir = 2;
      } else if (dir == 2) {
        for (int i = right - 1; i >= left; i--) {
          mat[bottom - 1][i] = val;
          val++;
        }
        bottom--;
        dir = 3;
      } else if (dir == 3) {
        for (int i = bottom - 1; i >= top; i--) {
          mat[i][left] = val;
          val++;
        }
        left++;
        dir = 0;
      }
    }
    return mat;
  }
};
