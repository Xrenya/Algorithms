#include <iostream>
#include <string>
#include <cassert>
#include <algorithm>

class Solution {
public:
    std::string maskPII(std::string s) {
        if (s.find('@') != std::string::npos) {
            return maskEmail(s);
        }
        return maskPhone(s);
    }
    std::string maskPhone(const std::string& s) {
        std::string output;
        std::string digits;
        for (auto ch : s) {
            if (isdigit(ch)) {
                digits += ch;
            }
        }

        if (digits.size() > 10) {
            output += '+';
            output += std::string(digits.size() - 10, '*');
            output += '-';
        }
        output += "***-***-";
        output += digits.substr(digits.size() - 4);
        return output;
    }
    std::string maskEmail(const std::string& s) {
        std::string output;
        int npos = s.find('@');

        output += tolower(s[0]);
        output += "*****";
        output += tolower(s[npos - 1]);
        for (auto ch : s.substr(npos)) {
            output += tolower(ch);
        }
        return output;
    }
};

int main() {
    Solution sol;
    std::string s = "LeetCode@LeetCode.com";
    std::string expected_output = "l*****e@leetcode.com";
    std::string output = sol.maskPII(s);
    
    assert((expected_output == output) && "Test #1 failed!");
    
    std::cout << "Tests are passed!" << std::endl;
    return 0;
}
