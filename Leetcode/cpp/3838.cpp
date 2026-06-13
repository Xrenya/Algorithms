#include <iostream>
#include <vector>
#include <string>
#include <cassert>

class Solution {
public:
    std::string mapWordWeights(std::vector<std::string>& words, std::vector<int>& weights) {
        std::string output;
        for (std::string word : words) {
            int index = 0;
            for (char ch : word) {
                index += weights[ch - 'a'];
            }
            index %= 26;
            output += ('z' - index);
        }
        return output;
    }
};

int main() {
    Solution sol;
    std::vector<std::string> words = {"abcd", "def", "xyz"};
    std::vector<int> weights = {5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2};
    std::string expectedOutput = "rij";
    std::string output = sol.mapWordWeights(words, weights);
    
    assert((output == expectedOutput) && "Test #1 failed!");
    std::cout << "Tests are passed!" << std::endl;
    return 0;
}
