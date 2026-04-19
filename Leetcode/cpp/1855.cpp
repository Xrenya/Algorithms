#include <iostream>
#include <vector>
#include <cassert>

class Solution {
public:
    int maxDistance(std::vector<int>& nums1, std::vector<int>& nums2) {
        int max_distance = -1;
        int index = 0;
        int size = nums1.size();
        for (int i = 0; i < nums2.size(); ++i) {
            while (index < size && nums1[index] > nums2[i]) {
                ++index;
            }
            if (index < size) {
                if (i >= index) {
                    max_distance = std::max(max_distance, i - index);
                }
            }
        }
        return max_distance == -1 ? 0 : max_distance;
    }
};
int main()
{
    Solution sol;
    std::vector<int> nums1 = {55,30,5,4,2}, nums2 = {100,20,10,10,5};
    int expected_output = 2;
    int output = sol.maxDistance(nums1, nums2);
    assert ((expected_output == output) && "Test 1");
    
    expected_output = 0;
    output = sol.maxDistance(nums1, nums1);
    assert ((expected_output == output) && "Test 2");
    
    expected_output = 1;
    output = sol.maxDistance(nums2, nums2);
    assert ((expected_output == output) && "Test 3");
    
    std::cout << "Tests are passed!" << std::endl;

    return 0;
}
