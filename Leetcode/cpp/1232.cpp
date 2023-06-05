class Solution {
public:
  float delta(int& p1, int& p2) {
    return p2 - p1;
  }
  bool checkStraightLine(vector<vector<int>>& coordinates) {
    float delta_x = delta(coordinates[0][0], coordinates[1][0]);
    float delta_y = delta(coordinates[0][1], coordinates[1][1]);
    for (int i = 2; i < coordinates.size(); i++) {
      if (delta_y * delta(coordinates[0][0], coordinates[i][0]) != delta_x * delta(coordinates[0][1], coordinates[i][1])) {
        return false;
      }
    }
    return true;
  }
};
