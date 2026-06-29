#include <iostream>
#include <string>
#include <vector>
#include <cassert>

class Solution {
public:
    int numOfStrings(std::vector<std::string>& patterns, std::string word) {
        int counter = 0;
        for (const std::string& pattern : patterns) {
            size_t position = word.find(pattern);
            if (position != std::string::npos) {
                ++counter;
            }
        }
        return counter;
    }
};


int main() {
    Solution sol;
    std::vector<std::string> patterns = {"a", "abc", "bc", "d"};
    std::string word = "abc";
    int expectedOutput = 3;
    int output = sol.numOfStrings(patterns, word);
    
    assert((expectedOutput == output) && "Test #1 failed!");
    std::cout << "All tests are passed!" << std::endl;
    return 0;
}
