#include <iostream>
#include <vector>
#include <cassert>

class Solution {
public:
    int p1 = 0, p2 = 0;

    int getMin(std::vector<int>& nums1, std::vector<int>& nums2) {
        int l1 = static_cast<int>(nums1.size());
        int l2 = static_cast<int>(nums2.size());
        
        if (p1 < l1 && p2 < l2) {
            return nums1[p1] < nums2[p2] ? nums1[p1++] : nums2[p2++];
        } else if (p1 < l1) {
            return nums1[p1++];
        } else if (p2 < l2) {
            return nums2[p2++];
        }
        return -1;
    }

    double findMedianSortedArrays(std::vector<int>& nums1, std::vector<int>& nums2) {
        int m = static_cast<int>(nums1.size()), n = static_cast<int>(nums2.size());
        
        if ((m + n) % 2 == 0) {
            for (int i = 0; i < (m + n) / 2 - 1; ++i) {
                int _ = getMin(nums1, nums2);
            }
            return (double)(getMin(nums1, nums2) + getMin(nums1, nums2)) / 2.0;

        } else {
            for (int i = 0; i < (m + n) / 2; ++i) {
                int _ = getMin(nums1, nums2);
            }
            return getMin(nums1, nums2);
        }

        return -1;
    }
};


int main() {
    Solution sol;
    std::vector<int> nums1 = {1,3}, nums2 = {2};
    double expected_output = 2.0;

    double output = sol.findMedianSortedArrays(nums1, nums2);
    assert(output == expected_output && "Test #1 failed!");

    std::cout << "Tests are passed!\n";
    return 0;
}
