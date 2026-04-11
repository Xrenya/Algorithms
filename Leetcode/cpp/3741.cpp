#include <iostream>
#include <vector>
#include <cassert>
#include <limits>
#include <unordered_map>


class NotOptimalSolution {
    int inf = std::numeric_limits<int>::max();

public:
    int minimumDistance(std::vector<int>& nums) {
        int n = nums.size();
        int output = inf;

        for (int i = 0; i < n - 2; ++i) {
            for (int j = i + 1; j < n - 1; ++j) {
                if (nums[i] != nums[j]) continue;
                for (int k = j + 1; k < n; ++k) {
                    if (nums[k] == nums[j]) {
                        output = std::min(output, abs(i - j) + abs(j - k) + abs(k - i));
                        break;
                    }
                }
            }
        } 
        return (output == inf) ? -1 : output;
    }
};

class Solution {
public:
    int minimumDistance(std::vector<int>& nums) {
        int n = nums.size();
        std::vector<int> next(n, -1);
        std::unordered_map<int, int> occur;
        int output = n + 1;
        for (int i = n - 1; i >= 0; --i) {
            if (occur.count(nums[i])) {
                next[i] = occur[nums[i]];
            }
            occur[nums[i]] = i;
        }

        for (int i = 0; i < n; ++i) {
            int secondPos = next[i];
             if (secondPos != -1) {
                int thirdPos = next[secondPos];
                if (thirdPos != -1) {
                    output = std::min(output, thirdPos - i);
                }
             }
        }
        return (output == n + 1) ? -1 : output * 2;
    }
};


int main() {
    NotOptimalSolution sol;
    int expected_output = 6;
    std::vector<int> nums = {1,2,1,1,3};
    int output = sol.minimumDistance(nums);
    assert (output == expected_output), "Output is not equal to expected_output";
    std::cout << "Test is passed! (NotOptimalSolution)" << std::endl;

  
    Solution opt_sol;
    output = opt_sol.minimumDistance(nums);
    assert (output == expected_output), "Output is not equal to expected_output";
    std::cout << "Test is passed! (Optimal Solution)" << std::endl;

    return 0;
}
