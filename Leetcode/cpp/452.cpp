class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        std::sort(
            points.begin(), points.end(),
            [](vector<int> a, vector<int> b) {
                if (a[1] < b[1]) {
                    return true;
                }
                return false;
            }
        );
        int counter = 1;
        int position = points[0].back();
        for (int i = 1; i < points.size(); ++i) {
            if (position < points[i][0]) {
                position = points[i][1];
                ++counter;
            }
        }

        return counter;
    }
};
