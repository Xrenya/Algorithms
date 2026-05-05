#include <iostream>
#include <vector>
#include <cassert>

class Solution {
public:
  std::vector<int> dailyTemperatures(std::vector<int>& temperatures) {
    int n = static_cast<int>(temperatures.size());
    std::vector<int> stack;
    std::vector<int> output(n, 0);
    for (int i = 0; i < n; ++i) {
      while (stack.size() > 0 && temperatures[stack[stack.size() - 1]] < temperatures[i]) {
        output[stack[stack.size() - 1]] = i - stack[stack.size() - 1];
        stack.pop_back();
      }
      stack.push_back(i);
    }
    return output;
  }
};

int main() {
  Solution sol;
  std::vector<int> temperatures = {73, 74, 75, 71, 69, 72, 76, 73};
  std::vector<int> expected_output = {1, 1, 4, 2, 1, 1, 0, 0};
  std::vector<int> output = sol.dailyTemperatures(temperatures);
  assert(output == expected_output && "Test #1 failed!");
  std::cout << "Tests are passed!" << std::endl;
}
