#include <vector>
#include <string>

class Solution {
public:
    std::vector<std::string> readBinaryWatch(int turnedOn) {
        std::vector<std::string> ans;
        
        for (int h = 0; h < 12; ++h) {
            for (int m = 0; m < 60; ++m) {
                
                int bits = 0;
                for (int temp_h = h; temp_h > 0; temp_h &= (temp_h - 1)) bits++;
                
                for (int temp_m = m; temp_m > 0; temp_m &= (temp_m - 1)) bits++;
                
                if (bits == turnedOn) {
                    ans.push_back(std::to_string(h) + ":" + (m < 10 ? "0" : "") + std::to_string(m));
                }
            }
        }
        return ans;
    }
};
