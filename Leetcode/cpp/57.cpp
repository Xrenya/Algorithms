class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        std::vector<std::vector<int>> output;
        int i = 0;
        for ( ; i < intervals.size(); ++i) {
            if (intervals[i][1] < newInterval[0]) {
                output.push_back(intervals[i]);
            } else {
                break;
            }
        }
        if (i == intervals.size()) {
            output.push_back(newInterval);
            return output;
        }
        if (intervals[i][0] > newInterval[0] && intervals[i][0] > newInterval[1]) {
            output.push_back(newInterval);
            output.push_back(intervals[i]);
        } else if (intervals[i][1] >= newInterval[0]) {
            output.push_back(
                {
                    std::min<int>(intervals[i][0], newInterval[0]),
                    std::max<int>(intervals[i][1], newInterval[1])
                }
            );
        }
        for (int j = i + 1; j < intervals.size(); ++j) {
            if (output.back()[1] >= intervals[j][0]) {
                output.back()[1] = std::max(output.back()[1], intervals[j][1]);
            } else {
                output.push_back(intervals[j]);
            }
        }
        return output;
    }
};
