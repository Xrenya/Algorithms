#include <iostream>
#include <string>
#include <cassert>
#include <algorithm>

class Solution {
public:
    char processStr(std::string s, long long k) {
        long long len = 0;
        for (auto c : s) {
            if (c == '*') {
                if (len) {
                    --len;
                }
            } else if (c == '#') {
                len *= 2;
            } else if (c == '%') {
                continue;
            } else {
                ++len;
            }
        }
        if (k + 1 > len) {
            return '.';
        }
        for (int i = s.size() - 1; i >= 0; --i) {
            if (s[i] == '*') {
                ++len;
            } else if (s[i] == '#') {
                if (k + 1 > (len + 1) / 2) {
                    k -= len / 2;
                }
                len = (len + 1) / 2;
            } else if (s[i] == '%') {
                k = len - k - 1;
            } else {
                if (k + 1 == len) {
                    return s[i];
                } else {
                    --len;
                }
            }
        }
        return '.';
    }
};

int main() {
    Solution sol;
    std::string s = "a#b%*";
    int k =1;
    char expectedOutput = 'a';
    
    char output = sol.processStr(s, k);
    assert((output == expectedOutput) && "Test #1 failed!");
    
    std::cout << "Tests are passed!" << std::endl;
    
    return 0;
}
