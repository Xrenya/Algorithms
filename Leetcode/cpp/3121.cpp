#include <iostream>
#include <unordered_map>
#include <set>
#include <cassert>
#include <string>
#include <vector>

class Solution {
public:
    int numberOfSpecialChars(std::string word) {
        std::unordered_map<char, int> umap;
        std::set<char> uset;
        for (int i = 0; i < static_cast<int>(word.length()); ++i) {
            char ch = word[i];
            if (std::isupper(ch) && !umap.contains(ch)) {
                umap[ch] = i;
            } else if (!std::isupper(ch)){
                umap[ch] = i;
            }
            if (std::islower(ch)) {
                uset.insert(ch);
            }
        }
        int output = 0;
        for (auto ch : uset) {
            if (umap.contains(std::toupper(ch))) {
                if (umap[std::toupper(ch)] > umap[ch]) {
                    ++output;
                }
            } 
        }
        return output;
    }
    
    int numberOfSpecialCharsWithArray(std::string word) {
        std::vector<int> alpha(52, -1);
        for (int i = 0; i < static_cast<int>(word.length()); ++i) {
            char ch = word[i];
            if (std::isupper(ch)) {
                if (alpha[ch - 'A' + 26] == -1) {
                    alpha[ch - 'A' + 26] = i;
                }
            } else {
                alpha[ch - 'a'] = i;
            }
        }
        int output = 0;
        for (int i = 0; i < 26; ++i) {
            if (alpha[i] != -1 && alpha[i + 26] > alpha[i]) {
                ++output;
            }
        }
        return output;
    }
};
int main() {
    Solution sol;
    std::string word = "aaAbcBC";
    int expectedOutput = 3;
    
    int output = sol.numberOfSpecialChars(word);
    assert((expectedOutput == output) && "Test #1 failed!");
    
    output = sol.numberOfSpecialCharsWithArray(word);
    assert((expectedOutput == output) && "Test #2 failed!");
    
    
    std::cout << "All tests are passed!" << std::endl;
    return 0;
}
