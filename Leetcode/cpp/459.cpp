#include <iostream>
#include <string>
#include <vector>
#include <cassert>
#include <algorithm>

class Solution {
public:
    // KMP solution
    bool repeatedSubstringPattern(std::string s) {
        int n = s.size();
        std::vector<int> lps(n, 0);  

        for (int i = 1, l = 0; i < n; ) {
            if (s[i] == s[l]) {
                lps[i++] = ++l; 
            } else if (l > 0) {
                l = lps[l - 1];
            } else {
                ++i;
            }
        }
        int l = lps[n - 1];
        return l > 0 && n % (n - l) == 0;
    }
    bool repeatedSubstringPatternAttach(std::string s) {
        int n = s.size();
        for (int i = 1; i < n / 2 + 1; ++i) {
            if (n % i == 0) {
                std::string repeated;
                for (int j = 0; j < n / i; ++j) {
                    repeated += s.substr(0, i);
                }
                if (repeated == s) return true;
            }
        }
        return false;
    }
};

int main() {
    Solution sol;
    std::string s = "abcabcabcabc";
    bool expected_output = true;
    
    bool output = sol.repeatedSubstringPattern(s);
    assert((expected_output == output) && "Test #1 failed!");
    
    output = sol.repeatedSubstringPatternAttach(s);
    assert((expected_output == output) && "Test #2 failed!");
    
    std::cout << "Tests are passed!" << std::endl;
    return 0;
}
