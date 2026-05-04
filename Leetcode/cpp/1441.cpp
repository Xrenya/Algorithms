#include <iostream>
#include <vector>
#include <cassert>
#include <climits>
#include <string>

class Solution {
public:
  std::vector<std::string> buildArray(std::vector<int>& target, int n) {
    if (target.size() == 0) {
      return {};
    }
    int prev = 1;
    std::vector<std::string> output;
    int size = static_cast<int>(target.size());
    int index = 0;
    while (index < size) {
      int n = target[index];
      if (n == prev) {
        output.push_back("Push");
        ++prev;
        ++index;
      } else {
        while (prev < n) {
            output.push_back("Push");
            output.push_back("Pop");
            ++prev;
        }
      }
    }
    return output;
  }
};

int main() {
  Solution sol;
  std::vector<int> target = {1, 3};
  int n = 3;
  std::vector<std::string> expected_output = {"Push", "Push", "Pop", "Push"};
  std::vector<std::string> output = sol.buildArray(target, n);
  assert(output == expected_output && "Test #1 failed!");
  std::cout << "Tests are passed!" << std::endl;
}
