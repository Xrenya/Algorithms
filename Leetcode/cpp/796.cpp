#include <iostream>
#include <string>
#include <cassert>
#include <vector>

class Solution {
public:
  bool rotateString(std::string s, std::string goal) {
    if (s.length() != goal.length()) {
        return false;
    }
    int n = static_cast<int>(s.length());

    for (int i = 0; i < n; ++i) {
      bool isValid = true;
      for (int j = 0; j < n; ++j) {
        if (s[(i + j) % n] != goal[j]) {
          isValid = false;
          break;
        }
      }
      if (isValid) {
        return true;
      }
    }
    return false;
  }
  
  bool rotateStringConcate(std::string s, std::string goal) {
    if (s.length() != goal.length()) {
        return false;
    }
    int n = static_cast<int>(s.length());
    s = s + s;

    return s.find(goal) != -1;
  }
  
    std::vector<int> preComputerLPS(std::string pattern) {
    int n = static_cast<int>(pattern.length());
    std::vector<int> lps(n, 0);
    int length = 0;
    int index = 1;
    while (index < n) {
      if (pattern[index] == pattern[length]) {
        ++length;
        lps[index] = length;
        ++index;
      } else if (length > 0) {
        length = lps[length - 1];
      } else {
        lps[index] = 0;
        ++index;
      }
    }
    return lps;
  }

  bool kmp(std::string text, std::string target, std::vector<int> lps) {
    int text_index = 0;
    int target_index = 0;
    int n = static_cast<int>(text.length());
    int target_length = static_cast<int>(target.length());
    while (text_index < n) {
      if (text[text_index] == target[target_index]) {
        text_index++;
        target_index++;
        if (target_index == target_length) {
          return true;
        }
      } else if (target_index > 0) {
        target_index = lps[target_index - 1];
      } else {
        ++text_index;
      }
    }
    return false;
  }

  bool rotateStringKMP(std::string s, std::string goal) {
    if (s.length() != goal.length()) {
      return false;
    }
    std::string double_string = s + s;
    std::vector<int> lps = preComputerLPS(goal);

    return kmp(double_string, goal, lps);       
  }
};

int main() {
    Solution sol;
    std::string s = "abcde", goal = "cdeab";
    bool expected_output = true;
    bool output = sol.rotateString(s, goal);
    
    assert (expected_output == output && "Test #1 failed!");
    
    output = sol.rotateStringConcate(s, goal);
    assert (expected_output == output && "Test #2 failed!");
    
    output = sol.rotateStringKMP(s, goal);
    assert (expected_output == output && "Test #3 failed!");
    std::cout << "Tests are passed!" << std::endl;
    
    return 0;
}
