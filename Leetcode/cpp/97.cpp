#include <iostream>
#include <vector>
#include <cassert>
#include <string>
#include <climits>

class Solution {
public:
  bool isInterleave(std::string s1, std::string s2, std::string s3) {
    if (s3.length() != s1.length() + s2.length()) {
      return false;
    }
    std::vector<std::vector<bool>> dp(s1.length() + 1, std::vector<bool>(s2.length() + 1));
    for (int i = 0; i <= s1.length(); ++i) {
      for (int j = 0; j <= s2.length(); ++j) {
        if (i == 0 && j == 0) {
          dp[i][j] = true;
        } else if (i == 0) {
          dp[i][j] = dp[i][j - 1] && s2[j - 1] == s3[i + j - 1];
        } else if (j == 0) {
          dp[i][j] = dp[i - 1][j] && s1[i - 1] == s3[i + j - 1];
        } else {
          dp[i][j] = (
            (dp[i - 1][j] && s1[i - 1] == s3[i + j - 1]) ||
            (dp[i][j - 1] && s2[j - 1] == s3[i + j - 1])
          );
        }
      }
    }
    return dp[s1.length()][s2.length()];
  }
};

int main() {
  Solution sol;
  std::string s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac";
  bool expected_output = true;
  bool output = sol.isInterleave(s1, s2, s3);
  assert ((expected_output == output) && "Test #1 failed!");
  std::cout << "Tests are passed!" << std::endl;
  
  return 0;
}
