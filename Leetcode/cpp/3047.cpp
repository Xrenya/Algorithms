#include <iostream>
#include <vector>

class Solution {
public:
    long long largestSquareArea(std::vector<std::vector<int>>& bottomLeft, std::vector<std::vector<int>>& topRight) {
        long long max = 0;
        for (std::vector<int>::size_type i = 0; i < bottomLeft.size(); ++i) {
            long long x_max_1 = topRight[i][0];
            long long y_max_1 = topRight[i][1];
            
            long long x_min_1 = bottomLeft[i][0];
            long long y_min_1 = bottomLeft[i][1];
            
            for (std::vector<int>::size_type j = i + 1; j < bottomLeft.size(); ++j) {
                long long x_max_2 = topRight[j][0];
                long long y_max_2 = topRight[j][1];
                
                long long x_min_2 = bottomLeft[j][0];
                long long y_min_2 = bottomLeft[j][1];

                long long x_bottom = std::max(x_min_1, x_min_2);
                long long y_bottom = std::max(y_min_1, y_min_2);

                long long x_top = std::min(x_max_1, x_max_2);
                long long y_top = std::min(y_max_1, y_max_2);

                if (x_bottom >= x_top || y_bottom >= y_top) {
                    continue;
                }
                long long dif_x = (x_top - x_bottom);
                long long dif_y = (y_top - y_bottom);
                long long min_size = std::min(dif_x, dif_y);
                max = std::max(max, min_size);
            }
        }
        return max * max;
    }
};
