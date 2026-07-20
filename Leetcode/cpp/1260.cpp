class Solution {
public:
    std::pair<int, int> toRowCol(int index, int rows, int cols) {
        int returnRow = index / cols;
        int returnCol = index % cols;
        return {returnRow, returnCol};
    }

    int toIndex(int row, int col, int rows, int cols) {
        int index = row * cols;
        return index + col;
    }

    std::vector<std::vector<int>> shiftGrid(std::vector<std::vector<int>>& grid, int k) {
        int rows = grid.size();
        int cols = grid[0].size();
        int size = rows * cols;
        k %= size;
        int count = 0;
        int index = 0;
        while (count < size) {
            int start = index;
            std::pair<int, int> position = toRowCol(start, rows, cols);
            int value = grid[position.first][position.second];
            while (true) {
                int nextIndex = (start + k) % size;
                position = toRowCol(nextIndex, rows, cols);
                int nextValue = grid[position.first][position.second];
                grid[position.first][position.second] = value;
                value = nextValue;
                start = nextIndex;
                ++count;
                if (start == index) {
                    break;
                }
            }
            ++index;
        }
        return grid;
    }
};
