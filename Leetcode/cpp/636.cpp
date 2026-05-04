#include <iostream>
#include <vector>
#include <cassert>
#include <climits>
#include <string>
#include <set>
#include <stack>

class Solution {
public:
  std::vector<int> exclusiveTime(int n, std::vector<std::string>& logs) {
    std::vector<int> output(n, 0);
    std::stack<int> stack;
    int prevTime = 0;

    for (const std::string& log : logs) {
      int firstCol = log.find(':');
      int lastCol = log.rfind(':');
      int id = std::stoi(log.substr(0, firstCol));
      std::string type = log.substr(firstCol + 1, lastCol - firstCol - 1);
      int timestamp = std::stoi(log.substr(lastCol + 1));

      if (type == "start") {
        if (!stack.empty()) {
            output[stack.top()] += timestamp - prevTime;
        }
        stack.push(id);
        prevTime = timestamp;
      } else {
        output[stack.top()] += timestamp - prevTime + 1;
        stack.pop();
        prevTime = timestamp + 1;
      }
    }
    return output;
  }
};

int main() {
  Solution sol;
  std::vector<std::string> logs = {"0:start:0", "1:start:2", "1:end:5", "0:end:6"};
  int n = 2;
  std::vector<int> expected_output = {3, 4};
  std::vector<int> output = sol.exclusiveTime(n, logs);
  assert(output == expected_output && "Test #1 failed!");
  std::cout << "Tests are passed!" << std::endl;
}
