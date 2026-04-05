#include <iostream>
#include <string>
#include <cassert>

class Solution {
public:
    bool judgeCircle(std::string moves) {
        int x = 0, y = 0;
        for (auto m : moves) {
            if (m == 'U') {
                y--;
            } else if (m == 'D') {
                y++;
            } else if (m == 'L') {
                x--;
            } else {
                x++;
            }
        }
        return x == 0 & y == 0;
    }
};


int main()
{
    Solution sol;
    assert (sol.judgeCircle("UD") == true);
    assert (sol.judgeCircle("UUD") == false);
    std::cout << "Tests are passed!" << std::endl;
    return 0;
}
