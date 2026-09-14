class Solution {
public:
    bool isRectangleOverlap(vector<int>& rec1, vector<int>& rec2) {
        int x0 = std::max<int>(rec1[0], rec2[0]);
        int y0 = std::max<int>(rec1[1], rec2[1]);
        int x1 = std::min<int>(rec1[2], rec2[2]);
        int y1 = std::min<int>(rec1[3], rec2[3]);
        return (x0 < x1 && y0 < y1);
    }
};
