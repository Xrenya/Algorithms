#include <iostream>
#include <cmath>
#include <climits>
#include <unordered_map>
#include <cassert>
#include <vector>

class Solution {
public:
    int minMirrorPairDistance(std::vector<int>& nums) {
        std::unordered_map<int, int> map;
        int minimum = INT_MAX;
        for (int i = 0; i < nums.size(); ++i) {
            int n = nums[i];
            int reverse = 0;
            int flag = 1;
            if (map.count(nums[i])) {  // map.find(x), map.contains(x)
                minimum = std::min(minimum, i - map[nums[i]]);
            }
            while (n > 0) {
                if (flag && (n % 10) == 0) {
                    n /= 10;
                } else {
                    flag = 0;
                    reverse = reverse * 10 + n % 10;
                    n /= 10;
                }
            }
            map[reverse] = i;
        }
        return minimum == INT_MAX ? -1 : minimum;
    }
};
int main()
{
    Solution sol;
    std::vector<int> input = {12,21,45,33,54};
    int expected_output = 1;
    assert (sol.minMirrorPairDistance(input) == expected_output);
    
    input = {120,21};
    expected_output = 1;
    assert (sol.minMirrorPairDistance(input) == expected_output);
    
    input = {21,120};
    expected_output = -1;
    assert (sol.minMirrorPairDistance(input) == expected_output);
    
    std::cout << "All tests are passed!" << std::endl;

    return 0;
}
