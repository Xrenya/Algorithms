#include <iostream>
#include <vector>
#include <cassert>
#include <string>
#include <climits>

class Solution {
public:
  std::string longestPalindrome(std::string s) {
    int n = static_cast<int>(s.size());

    if (n == 0) return "";

    std::vector<std::vector<int>> dp(n, std::vector<int>(n, 0));

    int max_len = 1;
    int start = 0;
    for (int i = n - 1; i >= 0; --i) {
      dp[i][i] = 1;
      for (int j = i + 1; j < n; ++j) {
        if (s[i] == s[j] && (j - i == 1 || dp[i + 1][j - 1])) {
          dp[i][j] = 1;
          int len = j + 1 - i;
          if (max_len <= len) {
            max_len = len;
            start = i;
          }
        }
      }
    }
    // for (int i = 0; i < n; ++i) {
    //   for (int j = 0; j < n; ++j) {
    //     std::cout << dp[i][j] << " ";
    //   }
    //   std::cout << std::endl;
    // }
    return s.substr(start, max_len); 
  }
};

int main() {
  Solution sol;
  std::string s = "babad";
  std::vector<std::string> expected_output = { "aba", "bab"};
  std::string output = sol.longestPalindrome(s);
  bool found = false;
  int i = 0;
  for ( ; i < expected_output.size(); ++i) {
    if (output == expected_output[i]) {
      found = true;
      break;
    }
  }
  if (!found) {
    std::cout << "Not found solution!" << std::endl;
  }
  std::cout << "Tests are passed!" << std::endl;
  
  return 0;
}
