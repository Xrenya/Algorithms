#include <iostream>
#include <climits>
#include <cassert>
#include <vector>
#include <functional>

class Solution {
public:
  std::vector<int> findBuildings(std::vector<int>& heights) {
    std::vector<int> output;
    int n = static_cast<int>(heights.size());
    int prev = 0;
    for (int i = n - 1; i >=0; --i) {
      if (prev < heights[i]) {
        output.push_back(i);
      }
      prev = std::max(prev, heights[i]);
    }
    std::reverse(output.begin(), output.end());
    return output; 
  }
};

int main() {
  std::vector<int> heights = {4,2,3,1};
  std::vector<int> expected_output = {0, 2, 3};
  Solution sol;
  std::vector<int> output = sol.findBuildings(heights);
  
  assert ((expected_output == output) && "Test #1 failed!");
  std::cout << "Tests are passed!" << std::endl;
  
  return 0;
}
