#include <iostream>
#include <vector>
#include <string>
#include <cctype>
#include <cassert>

class Solution {
public:
    int maxRepeating(std::string sequence, std::string word) {
        int output = 0;
        std::string tmp = word;
        while (sequence.find(tmp) != std::string::npos) {
            ++output;
            tmp += word;
        }
        return output;
    }
};

int main() {
    Solution sol;
    std::string sequence = "ababc", word = "ab";
    int expectedOutput = 2;
    int output = sol.maxRepeating(sequence, word);
    
    assert((expectedOutput == output) && "Test #1 failed!");
    std::cout << "Tests are passed!" << std::endl;
    return 0;
}
