#include <iostream>
#include <vector>
#include <cassert>

class Solution {
public:
    int maxDistance(std::vector<int>& colors) {
        int maxDist = 0;
        int size = colors.size();
        for (int i = 0; i < size; ++i) {
            if (colors[i] != colors[0]) {
                maxDist = std::max(maxDist, i);
            }
        }
        for (int i = 0; i < size; ++i) {
            if (colors[i] != colors[size - 1 - i]) {
                maxDist = std::max(maxDist, size - 1 - i);
            }
        }
        return maxDist;
    }
};

int main()
{
    Solution sol;
    std::vector<int> colors = {1,1,1,6,1,1,1};
    int expected_output = 3;
    int output = sol.maxDistance(colors);
    assert ((expected_output == output) && "Failed test #1");
    
    colors = {1,8,3,8,3};
    expected_output = 4;
    output = sol.maxDistance(colors);
    assert ((expected_output == output) && "Failed test #2");
    std::cout << "Tests are passed!" << std::endl;

    return 0;
}
