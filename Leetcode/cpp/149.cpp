#include <iostream>
#include <vector>
#include <cassert>
#include <algorithm>
#include <unordered_map>
#include <functional> // Required for std::hash

class Solution {
public:
    int gcd(int dx, int dy) {
        if (dy == 0) {
            return dx;
        }
        return gcd(dy, dx % dy);
    }
    int maxPoints(std::vector<std::vector<int>>& points) {
        int n = static_cast<int>(points.size());
        if (n == 1) {
            return 1;
        }
        int maxPoints = 2;
        for (int i = 0; i < n; ++i) {
            /*
            struct PairHash {
                size_t operator()(const std::pair<int, int>& p) const {
                    return std::hash<long long>()(
                        (static_cast<long long>(p.first) << 32) | 
                        (static_cast<long long>(p.second) & 0xFFFFFFFFLL)
                    );
                }
            };

            std::unordered_map<std::pair<int, int>, int, PairHash> umap;
            */
            std::map<std::pair<int, int>, int> umap;
            int cur_max = 1;
            for (int j = 0; j < n; ++j) {
                if (i == j) {
                    continue;
                }
                int dx = points[j][0] - points[i][0];
                int dy = points[j][1] - points[i][1];
                int g = gcd(dx, dy);
                std::pair<int, int> angle = {dx / g, dy / g};
                if (!umap.contains(angle)) {
                    umap[angle] = 0;
                }
                umap[angle] += 1;
                if (cur_max < umap[angle]) {
                    cur_max = umap[angle];
                }
            } 
            ++cur_max;
            if (maxPoints < cur_max) {
                maxPoints = cur_max;
            }
        }
        return maxPoints;
    }
};

int main() {
    Solution sol;
	std::vector<std::vector<int>> input = { {1, 1}, {2, 2},{3, 3} };
	int expected_output = 3;
	
	double output = sol.maxPoints(input);
	assert (expected_output == output && "Test #1 failed!");
	std::cout << "Tests are passed!" << std::endl;

}
