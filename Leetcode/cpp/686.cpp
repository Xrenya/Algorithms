#include <iostream>
#include <string>
#include <vector>
#include <cassert>
#include <algorithm>

class Solution {
public:
  int repeatedStringMatch(std::string a, std::string b) {
      std::string repeated;
      int count = 0;
      
      // Repeat until length is at least b.length()
      while (repeated.length() < b.length()) {
          repeated += a;
          count++;
      }
      
      // Check current
      if (repeated.find(b) != std::string::npos) return count;
      
      // Add one more and check
      repeated += a;
      if (repeated.find(b) != std::string::npos) return count + 1;
      
      return -1;
  }

    // Build LPS (Longest Prefix Suffix) array for KMP
    std::vector<int> computeLPS(const std::string& pattern) {
        int n = pattern.length();
        std::vector<int> lps(n, 0);
        int length = 0;
        int i = 1;
        
        while (i < n) {
            if (pattern[i] == pattern[length]) {
                length++;
                lps[i] = length;
                i++;
            } else if (length > 0) {
                length = lps[length - 1];
            } else {
                lps[i] = 0;
                i++;
            }
        }
        return lps;
    }
    
    // KMP search: returns true if target is in text
    bool kmpSearch(const std::string& text, const std::string& target, const std::vector<int>& lps) {
        int n = text.length();
        int m = target.length();
        int i = 0; // index for text
        int j = 0; // index for target
        
        while (i < n) {
            if (text[i] == target[j]) {
                i++;
                j++;
                if (j == m) {
                    return true; // Found
                }
            } else if (j > 0) {
                j = lps[j - 1];
            } else {
                i++;
            }
        }
        return false;
    }
    
    int repeatedStringMatchKMP(std::string a, std::string b) {
        int n = a.length();
        int m = b.length();
        
        // Precompute LPS for pattern b
        std::vector<int> lps = computeLPS(b);
        
        // Minimum repetitions needed to match length: ceil(m / n)
        int minRepeats = (m + n - 1) / n;
        
        // Build string with minRepeats copies of a
        std::string repeated;
        for (int i = 0; i < minRepeats; ++i) {
            repeated += a;
        }
        
        // Check if b is substring of minRepeats copies
        if (kmpSearch(repeated, b, lps)) {
            return minRepeats;
        }
        
        // Add one more copy (to handle cases where b spans the boundary)
        repeated += a;
        if (kmpSearch(repeated, b, lps)) {
            return minRepeats + 1;
        }
        
        // Add one more for safety (some edge cases need this)
        // Actually, theoretically max needed is minRepeats + 1, but let's be safe
        // or check up to minRepeats + 2 if a is very small compared to b
        // Actually, if not found in minRepeats + 1, it's impossible
        
        return -1;
    }
};

int main() {
    Solution sol;
    std::string a = "abcd", b = "cdabcdab";
    int expected_output = 3;
    
    int output = sol.repeatedStringMatchKMP(a, b);
    assert((expected_output == output) && "Test #1 failed!");
    
    output = sol.repeatedStringMatch(a, b);
    assert((expected_output == output) && "Test #2 failed!");
    
    std::cout << "Tests are passed!" << std::endl;
    return 0;
}
