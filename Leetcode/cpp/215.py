#include <iostream>
#include <cassert>
#include <vector>
#include <queue>

class Solution {
public:
    int findKthLargest(std::vector<int>& nums, int k) {
        std::priority_queue<int> pq;
        for (auto n : nums) {
            pq.push(n);
        }
        int val = pq.top();
        while (k) {
            val = pq.top();
            pq.pop();
            --k;
        }
        return val;
    }
};

int main()
{
    Solution sol;
    int expected_output = 5, k = 2;
    std::vector<int> input = {3,2,1,5,6,4};
    int output = sol.findKthLargest(input, k);
    assert (output == expected_output && "Tests are not passed!");
    
    std::cout << "Test are passed!";

    return 0;
}
