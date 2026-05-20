#include <iostream>
#include <vector>
#include <queue>
#include <cassert>

class Solution {
public:
    int lastStoneWeight(std::vector<int>& stones) {
        auto cmpMaxHeap = [](int a, int b) {
            return a < b;
        };

        std::priority_queue<int, std::vector<int>, decltype(cmpMaxHeap)> maxHeap(cmpMaxHeap);

        for (auto stone : stones) {
            maxHeap.push(stone);
        }

        while (maxHeap.size() >= 2) {
            int first = maxHeap.top();
            maxHeap.pop();
            int second = maxHeap.top();
            maxHeap.pop();
            if ((first - second) != 0) {
                maxHeap.push(first - second);
            }
        }
        return maxHeap.size() == 1 ? maxHeap.top() : 0;
    }
};

int main() {
    Solution sol;
    
    std::vector<int> stones = {2, 7, 4, 1, 8, 1};
    int expected_output = 1;
    
    int output = sol.lastStoneWeight(stones);
    assert((expected_output == output) && "Test #1 failed!");
    
    std::cout << "Tests are passed!" << std::endl;
    return 0;
}
