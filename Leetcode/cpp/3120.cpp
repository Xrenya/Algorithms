#include <iostream>
#include <vector>
#include <string>
#include <cctype>
#include <cassert>

class Solution {
public:
    int numberOfSpecialChars(std::string word) {
        std::vector<int> alpha(52, 0);
        int counter = 0;
        for (auto ch : word) {
            int tmp = 0;
            if (std::isupper(ch)) {
                alpha[26 + ch - 'A'] += 1;
                tmp += (alpha[26 + ch - 'A'] == 1) ? 1 : 0;
                tmp += (alpha[ch - 'A'] > 0) ? 1 : 0;
            } else {
                alpha[ch - 'a'] += 1;
                tmp += (alpha[ch - 'a'] == 1) ? 1 : 0;
                tmp += (alpha[26 + ch - 'a'] > 0) ? 1 : 0;
            }
            if (tmp == 2) {
                ++counter;
            }
        }
        return counter;
    }
};

int main() {
    Solution sol;
    std::string s = "aaAbcBC";
    int expectedOutput = 3;
    int output = sol.numberOfSpecialChars(s);
    
    assert((expectedOutput == output) && "Test #1 failed!");
    std::cout << "Tests are passed!" << std::endl;
    return 0;
}
