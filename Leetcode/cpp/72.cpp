#include <iostream>
#include <string>
#include <cassert>
#include <vector>
#include <map>
#include <numeric>  // iota

class Solution {
private:
  std::map<std::pair<int, int>, int> memo;

public:
  int dfsEdit(int i, int j, const std::string& word1, const std::string& word2) {
    if (i == 0) {
      return j;
    } else if (j == 0) {
      return i;
    }
    if (word1[i - 1] == word2[j - 1]) {
      return dfsEdit(i - 1, j - 1, word1, word2);
    }
    if (memo.contains({i, j})) {
      return memo[{i, j}];
    }
    int insertationOps = dfsEdit(i, j - 1, word1, word2);
    int deleteOps = dfsEdit(i - 1, j, word1, word2);
    int replaceOps = dfsEdit(i - 1, j - 1, word1, word2);
    memo[{i, j}] = std::min<int>(std::min<int>(insertationOps, deleteOps), replaceOps) + 1;
    return memo[{i, j}];
  }
  int minDistanceMap(std::string word1, std::string word2) {
    int i = static_cast<int>(word1.length());
    int j = static_cast<int>(word2.length());
    memo.clear();
    return dfsEdit(i, j , word1, word2);
  }
int minDistance(std::string word1, std::string word2) {
  // Ensure word1 is the shorter one for space optimization
  if (word1.size() > word2.size()) {
      std::swap(word1, word2);
  }
  
  int n = word1.size(), m = word2.size();
  std::vector<int> dp(n + 1), prev(n + 1);
  
  // Base case: word2 is empty
  std::iota(prev.begin(), prev.end(), 0); 

  for (int j = 1; j <= m; ++j) {
    dp[0] = j; // Base case: word1 is empty
    for (int i = 1; i <= n; ++i) {
      if (word1[i-1] == word2[j-1]) {
        dp[i] = prev[i-1];
      } else {
        dp[i] = 1 + std::min(std::min(prev[i], dp[i - 1]), prev[i - 1]);
      }
    }
    std::swap(dp, prev);
  }
  return prev[n];
  }
};


class SolutionTopDown {
    std::vector<std::vector<int>> memo;  // 2D Vector: O(1) access
    
    int dfsEdit(int i, int j, const std::string& word1, const std::string& word2) {
        if (i == 0) return j;
        if (j == 0) return i;
        
        // Check memo first
        if (memo[i][j] != -1) return memo[i][j];

        if (word1[i-1] == word2[j-1]) {
            return memo[i][j] = dfsEdit(i-1, j-1, word1, word2);
        }

        int insertOp = dfsEdit(i, j-1, word1, word2);
        int deleteOp = dfsEdit(i-1, j, word1, word2);
        int replaceOp = dfsEdit(i-1, j-1, word1, word2);
        
        return memo[i][j] = 1 + std::min<int>(insertOp, std::min<int>(deleteOp, replaceOp));
    }

public:
    int minDistance(std::string word1, std::string word2) {
        int n = word1.size(), m = word2.size();
        memo.assign(n + 1, std::vector<int>(m + 1, -1)); // Init with -1
        return dfsEdit(n, m, word1, word2);
    }
};

int main() {
  Solution sol;
  std::string word1 = "horse", word2 = "ros";
  int expected_output = 3;
  int output1 = sol.minDistance(word1, word2);
  
  assert (expected_output == output1 && "Test #1 failed!");
  
  int output2 = sol.minDistanceMap(word1, word2);
  assert (expected_output == output2 && "Test #2 failed!");
  
  SolutionTopDown solTopDown;
  int output3 = solTopDown.minDistance(word1, word2);
  assert (expected_output == output3 && "Test #3 failed!");
  std::cout << "Tests are passed!" << std::endl;
  
  return 0;
}
