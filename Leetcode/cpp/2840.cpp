#include <iostream>
#include <string>
#include <cassert>


class Solution {
public:
    bool checkStrings(std::string s1, std::string s2) {
        if (s1.length() != s2.length()) {
            return false;
        }
        int counts[256] = {0};

        for (int i = 0; i < s1.length(); ++i) {
            int offset = (i & 1) << 7;
            ++counts[offset + s1[i]];
            --counts[offset + s2[i]];
        }

        for (int i = 0; i < 256; ++i) {
            if (counts[i] != 0) {
                return false;
            }
        }
        return true;
    }
};


int main() {
	Solution sol;
	std::string s1 = "abcdba";
	std::string s2 = "cabdab";
	bool output = sol.checkStrings(s1, s2);
	std::cout << output << std::endl;
	assert (output == true);
	
	s1 = "abe";
	s2 = "bea";
	output = sol.checkStrings(s1, s2);
	std::cout << output << std::endl;
	assert (output == false);
	
	return 0;

}
