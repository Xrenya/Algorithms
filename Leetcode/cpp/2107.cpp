/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
#include <vector>
#include <unordered_map>
#include <cassert>

class Solution {
public:
    int shareCandies(std::vector<int>& candies, int k) {
        int unique = 0;

        std::unordered_map<int, int> flav;
        for (int c : candies) {
            if (++flav[c] == 1) {
                ++unique;
            }
        }

        int used = 0;
        for (int i = 0; i < k; ++i) {
            if (--flav[candies[i]] == 0) {
                ++used;
            }
        }

        int max = unique - used;
        for (int i = k; i < candies.size(); ++i) {
            if (++flav[candies[i - k]] == 1) {
                --used;
            }

            if (--flav[candies[i]] == 0) {
                ++used;
            }
            max = std::max<int>(max, unique - used);
        }
        return max;
    }
};

int main()
{
    Solution sol;
    std::vector<int> candies = {1, 2, 2, 3, 4, 3};
    int k = 3;
    int expectedOutput = 3;
    int output = sol.shareCandies(candies, k);
    assert((expectedOutput == output) && "Test #1 failed!");
    
    std::cout << "Tests are passed!" << std::endl;

    return 0;
}
