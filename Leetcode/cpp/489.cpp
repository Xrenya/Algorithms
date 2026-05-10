#include <iostream>
#include <vector>
#include <utility>  // std::pair<int, int>
#include <set>

/**
 * // This is the robot's control interface.
 * // You should not implement it, or speculate about its implementation
 * class Robot {
 *   public:
 *     // Returns true if the cell in front is open and robot moves into the cell.
 *     // Returns false if the cell in front is blocked and robot stays in the current cell.
 *     bool move();
 *
 *     // Robot will stay in the same cell after calling turnLeft/turnRight.
 *     // Each turn will be 90 degrees.
 *     void turnLeft();
 *     void turnRight();
 *
 *     // Clean the current cell.
 *     void clean();
 * };
 */

class Solution {
public:
  void getBack(Robot& robot) {
    robot.turnRight();
    robot.turnRight();
    robot.move();
    robot.turnRight();
    robot.turnRight();
  }

  void cleanRoom(Robot& robot) {
    std::vector<std::pair<int, int>> directions = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
    std::set<std::pair<int, int>> visited;

    std::function<void(std::pair<int, int>, int)> dfs = [&](std::pair<int, int> cell, int d) -> void {
      visited.emplace(cell);
      robot.clean();

      for (int i = 0; i < 4; ++i) {
        int new_d = (d + i) % 4;
        std::pair<int, int> newCell = {cell.first + directions[new_d].first, cell.second + directions[new_d].second};

        if (!visited.contains(newCell) && robot.move()) {
          dfs(newCell, new_d);
          getBack(robot);
        }
        robot.turnRight();

      }
    };
    dfs({0, 0}, 0);
  }
};
