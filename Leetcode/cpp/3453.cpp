#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

class Solution {
public:
    double separateSquares(vector<vector<int>>& squares) {
        double total_area = 0;
        double min_y = 2e9, max_y = 0;

        for (const auto& sq : squares) {
            double y = sq[1], l = sq[2];
            total_area += l * l;
            min_y = min(min_y, y);
            max_y = max(max_y, y + l);
        }

        auto check = [&](double mid) {
            double area_below = 0;
            for (const auto& sq : squares) {
                double y = sq[1], l = sq[2];
                if (mid <= y) continue;
                if (mid >= y + l) {
                    area_below += l * l;
                } else {
                    area_below += l * (mid - y);
                }
            }
            return area_below >= total_area / 2.0;
        };

        double lo = min_y, hi = max_y;
        for (int i = 0; i < 50; ++i) {
            double mid = lo + (hi - lo) / 2;
            if (check(mid)) {
                hi = mid;
            } else {
                lo = mid;
            }
        }

        return hi;
    }
};
