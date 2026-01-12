#include <iostream>
#include <vector>


class Solution {
public:
    int minTimeToVisitAllPoints(std::vector<std::vector<int>>& points) {
        int output = 0;
        for (std::vector<int>::size_type i = 0; i < points.size() - 1; ++i) {
            output += std::max(
                std::abs(
                    points[i][0] - points[i + 1][0]
                ),
                std::abs(
                    points[i][1] - points[i + 1][1]
                )
            );
        }
        return output;
    }
};
