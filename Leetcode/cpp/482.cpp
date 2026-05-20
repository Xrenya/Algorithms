#include <iostream>
#include <string>
#include <cassert>
#include <algorithm>

class Solution {
public:
    std::string licenseKeyFormatting(std::string s, int k) {
        std::string output;
        int cur = 0;
        int n = s.length();
        for (int i = n - 1; i >= 0; --i) {
            if (s[i] != '-') {
                if (cur < k) {
                    ++cur;
                } else {
                    output += '-';
                    cur = 1;
                }
                output += toupper(s[i]);
            }
        }
        std::reverse(output.begin(), output.end());
        return output;
    }
};

int main() {
    Solution sol;
    std::string s = "5F3Z-2e-9-w";
    int k = 4;
    std::string expected_output = "5F3Z-2E9W";
    std::string output = sol.licenseKeyFormatting(s, k);
    assert(output == expected_output && "Test #1 failed!");

    std::cout << "Tests are passed!\n";
    return 0;
}
