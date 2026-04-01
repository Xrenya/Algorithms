#include <iostream>
#include <vector>
#include <string>
#include <cassert>

class Solution {
public:
    int minOperations(std::vector<std::string>& logs) {
        int depth = 0;
        
        // Use const auto& to avoid copying strings
        for (const auto& log : logs) {
            if (log == "./") {
                continue;
            } else if (log == "../") {
                if (depth > 0) {
                    depth--;
                }
            } else {
                // It's a folder name like "d1/", go deeper
                depth++;
            }
        }
        return depth;
    }
};

int main() {
    Solution sol;
    
    std::vector<std::string> logs1 = {"d1/","d2/","../","d21/","./"};
    assert(sol.minOperations(logs1) == 2);

    // Test Case 2: Edge case (staying at root)
    std::vector<std::string> logs2 = {"../", "../", "../"};
    assert(sol.minOperations(logs2) == 0);

    // Test Case 3: Nested deep
    std::vector<std::string> logs3 = {"a/", "b/", "c/", "d/"};
    assert(sol.minOperations(logs3) == 4);

    std::cout << "All tests passed!" << std::endl;
    
    return 0;
}
