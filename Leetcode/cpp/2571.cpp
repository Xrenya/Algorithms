#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <cassert>
#include <algorithm>


class Solution {
public:
    std::vector<int> survivedRobotsHealths(std::vector<int>& positions, std::vector<int>& healths, std::string directions) {
        int n = positions.size();
        std::vector<int> indices(n), output;
        std::stack<int> stack;

        for (int i = 0; i < n; ++i) {
            indices[i] = i;
        }

        sort(
            indices.begin(), indices.end(), [&](int l, int r) { return positions[l] < positions[r]; }
        );

        for (int idx : indices) {
            if (directions[idx] == 'R') {
                stack.push(idx);
            } else {
                while (!stack.empty() && healths[idx] > 0) {
                    int top_idx = stack.top();
                    stack.pop();

                    if (healths[top_idx] > healths[idx]) {
                        healths[idx] = 0;
                        healths[top_idx] -= 1;
                        stack.push(top_idx);
                    } else if (healths[idx] > healths[top_idx]) {
                        healths[top_idx] = 0;
                        healths[idx] -= 1;
                    } else {
                        healths[top_idx] = 0;
                        healths[idx] = 0;
                    }
                }
            }
        }
        for (int i = 0; i < n; ++i) {
            if (healths[i] > 0) {
                output.push_back(healths[i]);
            }
        }
        return output;
    }
};


int main() {
    Solution sol;
    std::vector<int> positions = {5,4,3,2,1}, healths = {2,17,9,15,10}, expected_output = {2,17,9,15,10}, output;
    std::string directions = "RRRRR";
    output = sol.survivedRobotsHealths(positions, healths, directions);
    for (int i = 0; i < output.size(); ++i) {
        std::cout << output[i] << " ";
    }
    std::cout << std::endl;
    for (int i = 0; i < expected_output.size(); ++i) {
        std::cout << expected_output[i] << " ";
    }
    std::cout << std::endl;
    assert (output == expected_output);
    return 0;
}
