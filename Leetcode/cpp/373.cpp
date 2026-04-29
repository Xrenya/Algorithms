#include <iostream>
#include <vector>
#include <cassert>
#include <utility>
#include <set>
#include <queue>

class Solution {
public:
    std::vector<std::vector<int>> kSmallestPairs(std::vector<int>& nums1, std::vector<int>& nums2, int k) {
        int m = nums1.size();
        int n = nums2.size();

        std::vector<std::vector<int>> output;
        std::set<std::pair<int, int>> visited;

        std::priority_queue<std::pair<int, std::pair<int, int>>, std::vector<std::pair<int, std::pair<int, int>>>,
                       std::greater<std::pair<int, std::pair<int, int>>>> minHeap;
        minHeap.push({nums1[0] + nums2[0], {0, 0}});
        visited.insert({0, 0});

        while (k-- && !minHeap.empty()) {
            auto top = minHeap.top();
            minHeap.pop();
            int i = top.second.first;
            int j = top.second.second;

            output.push_back({nums1[i], nums2[j]});

            if (i + 1 < m && visited.find({i + 1, j}) == visited.end()) {
                minHeap.push({nums1[i + 1] + nums2[j], {i + 1, j}});
                visited.insert({i + 1, j});
            }
            if (j + 1 < n && visited.find({i, j + 1}) == visited.end()) {
                minHeap.push({nums1[i] + nums2[j + 1], {i, j + 1}});
                visited.insert({i, j + 1});
            }
        }
        return output;
    }
};

int main() {
    Solution sol;
    std::vector<int> nums1 = {1,7,11}, nums2 = {2,4,6};
    int k = 3;
    std::vector<std::vector<int>> expected_output = {{1,2},{1,4},{1,6}};
    std::vector<std::vector<int>> output = sol.kSmallestPairs(nums1, nums2, k);
    assert(output == expected_output && "Test #1 failed!");

    std::cout << "Tests are passed!\n";
    return 0;
}
