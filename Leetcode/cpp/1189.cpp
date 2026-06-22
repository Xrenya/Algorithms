#include <iostream>
#include <climits>
#include <string>
#include <cassert>
#include <unordered_map>

class Solution {
public:
    int maxNumberOfBalloons(std::string text) {
        std::unordered_map<char, int> umap;
        for (auto chr : text) {
            umap[chr] += 1;
        }
        std::string word = "balloon";
        int minLetters = INT_MAX;
        int counter = 0;
        for (auto chr : word) {
            if (!umap.contains(chr)) {
                return 0;
            } else {
                counter = umap[chr];
                if (chr == 'l' || chr == 'o') {
                    counter /= 2;
                }
            }
            minLetters = std::min<int>(minLetters, counter);
        }
        return minLetters;
    }
};

int main() {
    Solution sol;
    std::string text = "loonbalxballpoon";
    int expectedOutput = 2;
    int output = sol.maxNumberOfBalloons(text);
    
    assert((output == expectedOutput) && "Test #1 failed!");
    std::cout << "Tests are passed!" << std::endl;
    return 0;
}
