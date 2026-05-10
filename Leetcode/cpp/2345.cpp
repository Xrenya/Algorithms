#include <iostream>
#include <climits>
#include <cassert>
#include <vector>
#include <functional>

class Solution {
public:
  int visibleMountains(std::vector<std::vector<int>>& peaks) {
    std::vector<std::pair<int, int>> intervals;
    for (auto& peak : peaks) {
      int x = peak[0];
      int y = peak[1];
      int left = x - y;
      int right = x + y;
      intervals.emplace_back(left, -right);
    }

    std::sort(intervals.begin(), intervals.end());

    int n = static_cast<int>(intervals.size());
    int visibleCount = 0;
    int maxRightBoundary = INT_MIN;

    for (int i = 0; i < n; ++i) {
      int left = intervals[i].first;
      int right = -intervals[i].second;

      if (right <= maxRightBoundary) {
        continue;
      }
      maxRightBoundary = right;

      bool isLast = (i == n - 1);
      bool isDifferent = (i < n - 1 && intervals[i] != intervals[i + 1]);

      if (isLast || isDifferent) {
        ++visibleCount;
      }
    }
    return visibleCount;
  }
};

int main() {
  std::vector<std::vector<int>> peaks  = { {2, 2}, {6, 3}, {5, 4} };
  int expected_output = 2;
  Solution sol;
  int output = sol.visibleMountains(peaks);
  
  assert ((expected_output == output) && "Test #1 failed!");
  std::cout << "Tests are passed!" << std::endl;
  
  return 0;
}
