#include <iostream>
#include <vector>
#include <cassert>
#include <algorithm>

class Solution {
public:
    int maxBuilding(int n, std::vector<std::vector<int>>& restrictions) {
        auto&& r = restrictions;
        r.push_back({1, 0});
        std::sort(r.begin(), r.end());

        if (r.back()[0] != n) {
            r.push_back({n, n - 1});
        }

        int m = r.size();

        for (int i = 1; i < m; ++i) {
            r[i][1] = std::min<int>(r[i][1], r[i - 1][1] + (r[i][0] - r[i - 1][0]));
        }

        for (int i = m - 2; i >= 0; --i) {
            r[i][1] = std::min<int>(r[i][1], r[i + 1][1] + (r[i + 1][0] - r[i][0]));
        }

        int output = 0;

        for (int i = 0; i < m - 1; ++i) {
            int best = ((r[i + 1][0] - r[i][0]) + r[i][1] + r[i + 1][1]) / 2;
            output = std::max<int>(best, output);
        }
        return output;
    }
};

int main() {
    Solution sol;
    int n = 5;
    std::vector<std::vector<int>> restrictions = {{2, 1}, {4, 1}};
    int expectedOutput = 2;
    int output = sol.maxBuilding(n, restrictions);
    assert((output == expectedOutput) && "Test #1 failed!");
    std::cout << "Tests are passed!" << std::endl;
    return 0;
}
