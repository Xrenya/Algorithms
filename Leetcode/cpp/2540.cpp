#include <iostream>
#include <vector>
#include <cassert>

class Solution {
public:
    int getCommon(std::vector<int>& nums1, std::vector<int>& nums2) {
        int n = static_cast<int>(nums1.size());
        int m = static_cast<int>(nums2.size());
        int i = 0;
        int j = 0;
        while (i < n && j < m) {
            if (nums1[i] == nums2[j]) {
                return nums1[i];
            } else if (nums1[i] < nums2[j]) {
                ++i;
            } else {
                ++j;
            }
        }
        return -1;
    }
};

int main() {
    Solution sol;
    std::vector<int> nums1 = {1, 2, 3, 6};
    std::vector<int> nums2 = {2, 3, 4, 5};
    int expected_output = 2;
    int output = sol.getCommon(nums1, nums2);
    
    assert((expected_output == output) && "Test #1 failed!");
    
    std::cout << "Tests are passed!" << std::endl;
    return 0;
}
