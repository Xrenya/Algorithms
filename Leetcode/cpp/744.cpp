#include <iostream>
#include <vector>

class Solution {
public:
    char nextGreatestLetter(std::vector<char>& letters, char target) {
        for (auto chr : letters) {
            if (chr > target) {
                return chr;
            }
        }
        return letters[0];
    }
};
