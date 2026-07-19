#include <iostream>
#include <vector>
#include <cassert>

class SolutionV2 {
public:
    int findMin(std::vector<int>& nums) {
        int left = 0;
        int right = static_cast<int>(nums.size()) - 1; 
        
        while (left < right) {
            int m = left + (right - left) / 2;
            
            if (nums[m] > nums[right]) {
                left = m + 1;
            } else {
                right = m;
            }
        }
        
        return nums[left];
    }
};


class Solution {
public:
    int findMin(std::vector<int>& nums) {
        int n = static_cast<int>(nums.size());
        int left = 0;
        int right = n - 1;
        while (left < right) {
          int m = left + (right - left) / 2;
          if (nums[m] > nums[n - 1]) {
            left = m + 1;
          } else {
            right = m;
          }
        }
        return nums[left];
    }
};


int main() {
    Solution sol;
    std::vector<int> nums = {5, 6, 1, 2, 3, 4};
    int exected_output = 1;
    int output = sol.findMin(nums);
    
    assert((output == exected_output) && "Test #1 failed!");
    
    
    nums = {6, 5, 4, 3};
    exected_output = 3;
    output = sol.findMin(nums);
    assert((output == exected_output) && "Test #2 failed!");
    
    
    nums = {1, 2, 3, 4, 5, 6};
    exected_output = 1;
    output = sol.findMin(nums);
    assert((output == exected_output) && "Test #2 failed!");
    
    std::cout << "Tests are passed!" << std::endl;
    
    return 0;
}

