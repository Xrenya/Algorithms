#include <iostream>
#include <string>


class Solution {
public:
    string addBinary(std::string a, std::string b) {
        int asz = a.size() - 1;
        int bsz = b.size() - 1;
        int cur = 0;
        std::string output = "";
        while (asz >= 0 || bsz >= 0 || cur > 0) {
            if (asz >= 0) cur += a[asz--] - '0';
            if (bsz >= 0) cur += b[bsz--] - '0';
            output = char(cur % 2 + '0') + output;
            cur = cur / 2;
        }
        return output;
    }
};
