#include <iostream>
#include <string>
#include <cassert>

class Solution {
public:
    bool detectCapitalUse(std::string word) {
        int n = word.length();
        int first = 0;
        int all = 0;
        int lower = 0;
        for (int i = 0; i < n; ++i) {
            char ch = word[i];
            if (i == 0) {
                if (ch >= 'A' && ch <= 'Z') {
                    first = 1;
                }
            }
            if (ch >= 'A' && ch <= 'Z') {
                ++all;
            } else {
                ++lower;
            }
        }
        if (all == n || (first && ((lower + 1) == n)) || lower == n) {
            return true;
        }
        return false;
    }
};

int main() {
    Solution sol;
    std::string word = "FlaG";
    bool expected_output = false;
    bool output = sol.detectCapitalUse(word);
    assert(output == expected_output && "Test #1 failed!");

    std::cout << "Tests are passed!\n";
    return 0;
}
