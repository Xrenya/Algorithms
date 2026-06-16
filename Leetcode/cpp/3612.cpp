#include <iostream>
#include <string>
#include <cassert>
#include <algorithm>

class Solution {
public:
    std::string processStr(std::string s) {
        std::string output;
        for (auto chr : s) {
            if (chr == '*') {
                if (output.size()) {
                    output.pop_back();
                }
            } else if (chr == '#') {
                output += output;
            } else if (chr == '%') {
                std::reverse(output.begin(), output.end());
            } else {
                output += chr;
            }
        }
        return output;
    }
};

int main() {
    Solution sol;
    std::string s = "a#b%*";
    std::string expectedOutput = "ba";
    
    std::string output = sol.processStr(s);
    assert((output == expectedOutput) && "Test #1 failed!");
    
    std::cout << "Tests are passed!" << std::endl;
    
    return 0;
}
