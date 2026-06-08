#include <iostream>
#include <vector>
#include <cassert>

class Solution {
public:
    std::vector<int> pivotArrayNotGood(std::vector<int>& nums, int pivot) {
        std::vector<int> less, eq, greater;
        for (auto num : nums) {
            if (num < pivot) {
                less.push_back(num);
            } else if (num == pivot) {
                eq.push_back(num);
            } else {
                greater.push_back(num);
            }
        }
        std::vector<int> output;
        for (auto num : less)  {
            output.push_back(num);
        }
        for (auto num : eq)  {
            output.push_back(num);
        }
        for (auto num : greater)  {
            output.push_back(num);
        }
        return output;
    }
    
    std::vector<int> pivotArray(std::vector<int>& nums, int pivot) {
        int less = 0;
        int equal = 0;
        for (int num : nums) {
            if (num < pivot)
                less++;
            else if (num == pivot)
                equal++;
        }

        std::vector<int> ans(nums.size());
        int lessI = 0;
        int equalI = less;
        int greaterI = less + equal;
        for (int i = 0; i < nums.size(); i++) {
            int num = nums[i];
            if (num < pivot) {
                ans[lessI] = num;
                lessI++;
            } else if (num > pivot) {
                ans[greaterI] = num;
                greaterI++;
            } else {
                ans[equalI] = num;
                equalI++;
            }
        }
        return ans;
    }
    
};

int main(void)
{
    Solution sol;
    std::vector<int> nums = {9, 12, 5, 10, 14, 3, 10};
    int pivot = 10;
    std::vector<int> expectedOutput = {9, 5, 3, 10, 10, 12, 14};
    
    std::vector<int> output = sol.pivotArrayNotGood(nums, pivot);
    assert((output == expectedOutput) && "Test #1 failed!");
    
    output = sol.pivotArray(nums, pivot);
    assert((output == expectedOutput) && "Test #2 failed!");
    
    std::cout << "Tests are passed!" << std::endl;
    
    return 0;
}
