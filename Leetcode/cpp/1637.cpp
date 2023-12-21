class Solution {
public:
    int maxWidthOfVerticalArea(vector<vector<int>>& points) {
        std::sort(points.begin(), points.end());
        
        int output = 0;
        for (int i = 1; i < points.size(); i++) {
            output = std::max(output, points[i][0] - points[i - 1][0]);
        }
        return output;
    }
};
