#include <iostream>
#include <vector>
#include <cassert>

class Solution {
public:
    // search in [left, right]
    int binarySearch(std::vector<int>& nums, int left, int right, int target) {
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) return mid;
            else if (nums[mid] < target) left = mid + 1;
            else right = mid - 1;
        }
        return -1;
    }

    int search(std::vector<int>& nums, int target) {
        int n = nums.size();
        if (n == 0) return -1;

        int left = 0, right = n - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        int pivot = left;

        if (target >= nums[pivot] && target <= nums[n - 1]) {
            return binarySearch(nums, pivot, n - 1, target);
        } else {
            return binarySearch(nums, 0, pivot - 1, target);
        }
    }
};

int main(void) {
    Solution sol;
    std::vector<int> input = {4,5,6,7,0,1,2};
    int target = 0;
    int expected_output = 4;
    int output = sol.search(input, target);
    assert ((expected_output == output) &&  "Test #1 is not passed!");   
    std::cout << "Tests are passed!" << std::endl;
    return 0;
}
