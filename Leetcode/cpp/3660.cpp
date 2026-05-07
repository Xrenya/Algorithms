#include <iostream>
#include <vector>
#include <string>
#include <cassert>


class Solution {
public:
    struct Item {
        int value;
        int left;
        int right;
    };

    std::vector<int> maxValue(const std::vector<int>& nums) {
        int n = nums.size();
        std::vector<int> output(n, 0);
        
        std::vector<Item> stack;

        for (int i = 0; i < n; ++i) {
            Item cur = {nums[i], i, i};

            while (!stack.empty() && stack.back().value > nums[i]) {
                Item top = stack.back();
                stack.pop_back();
                cur.value = std::max<int>(cur.value, top.value);
                cur.left = top.left;
            }
            stack.push_back(cur);
        }

        for (size_t  i = 0; i < stack.size(); ++i) {
            for (int j = stack[i].left; j <= stack[i].right; ++j) {
                output[j] = stack[i].value;
            }
        }
        return output;
    }
};


int main() {
    Solution sol;
    std::vector<int> nums = {2, 1, 3};
    std::vector<int> expected_output = {2, 2, 3};
    
    std::vector<int> output = sol.maxValue(nums);
    assert ((expected_output == output) && "Test #1 failed!");

    std::cout << "Tests are passed!" << std::endl;
    
    return 0;
}
