class Solution {
public:
    int removeCoveredIntervals(vector<vector<int>>& intervals) {
        std::sort(
            intervals.begin(),
            intervals.end(),
            [](vector<int> a, vector<int> b) {
                if (a[0] < b[0]) {
                    return true;
                } else if (a[0] == b[0]) {
                    return a[1] > b[1];
                }
                return false;
            }
        );
        if (intervals.size() == 0) return 0;

        vector<int> prev = intervals[0];
        int output = 1;
        for (size_t i = 1; i < intervals.size(); ++i) {
            if (prev[0] <= intervals[i][0] && prev[1] >= intervals[i][1]) {
                continue;
            } else {
                prev = intervals[i];
                ++output;
            }
        }
        return output;
    }
};
