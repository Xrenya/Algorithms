#include <iostream>
#include <string>
#include <vector>
#include <cassert>


class Solution {
public:
    int numberOfSubstrings(std::string s) {
        int len = s.length();
        int left = 0, right = 0;
        std::vector<int> freq(3, 0);
        int total = 0;

        while (right < len) {
            char cur = s[right];
            ++freq[cur - 'a'];

            while (hasAllChars(freq)) {
                total += len - right;

                char leftChar = s[left];
                --freq[leftChar - 'a'];
                ++left;
            }

            ++right;
        }

        return total;
    }

private:
    bool hasAllChars(std::vector<int>& freq) {
        return freq[0] > 0 && freq[1] > 0 && freq[2] > 0;
    }
};

int main() {
    Solution sol;
    std::string s = "abcabc";
    int expectedOutput = 10;
    
    int output = sol.numberOfSubstrings(s);
    assert((expectedOutput == output) && "Test #1 failed!");
    
    std::cout << "Tests are passed!" << std::endl;

    return 0;
}
