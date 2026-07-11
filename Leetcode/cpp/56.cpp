class Solution {
public:
    std::vector<std::vector<int>> merge(std::vector<std::vector<int>>& intervals) {
        if (intervals.empty()) return {};

        std::sort(
            intervals.begin(),
            intervals.end(),
            [](const std::vector<int>& a, const std::vector<int>& b) {
                if (a[0] < b[0]) {
                    return true;
                } else if (a[0] == b[0] && a[1] > b[1]) {
                    return true;
                }
                return false;
            }
        );
        std::vector<std::vector<int>> output = {intervals[0]};
        for (int i = 1; i < intervals.size(); ++i) {
            if (output.back()[1] >= intervals[i][0]) {
                output.back()[1] = std::max<int>(output.back()[1], intervals[i][1]);
            } else {
                output.push_back(intervals[i]);
            }
        }

        return output;
    }
};
