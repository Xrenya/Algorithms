/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

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
