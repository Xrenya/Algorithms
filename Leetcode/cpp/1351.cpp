class Solution {
public:
  int binsearch(vector<int>& array) {
    int left = -1, right = array.size(), mid, len = array.size();
    while (left < right - 1) {
      int m = left + (right - left) / 2;
      if (array[m] >= 0) {
        left = m;
      } else {
        right = m;
      }
    }
    return len - left - 1;
  }
  int countNegatives(vector<vector<int>>& grid) {
    int count = 0;
    for (int i = 0; i < grid.size(); i++) {
      count += binsearch(grid[i]);
    }
    return count;
  }
};
