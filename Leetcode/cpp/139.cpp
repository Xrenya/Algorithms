#include <iostream>
#include <vector>
#include <cassert>
#include <string>

class Solution {
public:
  bool wordBreak(std::string s, std::vector<std::string>& wordDict) {
    int n = static_cast<int>(s.size());
    std::vector<int> dp(n + 1, false);

    dp[0] = true;  // base

    for (int i = 1; i <= n; ++i) {
      for (auto word : wordDict) {
        int len = static_cast<int>(word.size());

        if (i >= len && dp[i - len]) {
          if (s.compare(i - len, len, word) == 0) {
            dp[i] = true;
            break;
          }
        }
      }
    }
    return dp[n];
  }
};


int main() {
  Solution sol;
  std::string s = "leetcode";
  std::vector<std::string> wordDict = {"leet","code"};
  bool expected_output = true;
  bool output = sol.wordBreak(s, wordDict);
  assert ((output == expected_output) && "Test #1 failed!");
  std::cout << "Tests are passed!" << std::endl;
  
  return 0;
}
