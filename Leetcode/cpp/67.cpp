#include <iostream>
#include <string>
#include <cassert>
#include <queue>
#include <algorithm>

class Solution {
public:
    std::string addBinary(std::string a, std::string b) {
        int i = static_cast<int>(a.size()) - 1;
        int j = static_cast<int>(b.size()) - 1;
        int carry = 0;
        std::string output;
        while (i >= 0 || j >= 0 || carry > 0) {
            if (i >= 0) {
                carry += (a[i--] - '0');
            }
            if (j >= 0) {
                carry += (b[j--] - '0');
            }
            output.push_back((carry % 2) ? '1' : '0');
            carry /= 2;
        }
        std::reverse(output.begin(), output.end());
        return output;
    }

    std::string addBinaryNotOptimal(std::string a, std::string b) {
        int asz = a.size() - 1;
        int bsz = b.size() - 1;
        int cur = 0;
        std::string output = "";
        while (asz >= 0 || bsz >= 0 || cur > 0) {
            if (asz >= 0) cur += a[asz--] - '0';
            if (bsz >= 0) cur += b[bsz--] - '0';
            output = char(cur % 2 + '0') + output;
            cur = cur / 2;
        }
        return output;
    }
};
int main() {
    Solution sol;
    std::string a = "11";
    std::string b = "1";
    std::string expected_output = "100";
    std::string output = sol.addBinary(a, b);
    
    assert(output == expected_output && "Test #1 failed!");
    std::cout << "Tests are passed!\n";
    return 0;
}
