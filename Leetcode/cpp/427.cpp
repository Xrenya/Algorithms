/*
// Definition for a QuadTree node.
class Node {
public:
    bool val;
    bool isLeaf;
    Node* topLeft;
    Node* topRight;
    Node* bottomLeft;
    Node* bottomRight;
    
    Node() {
        val = false;
        isLeaf = false;
        topLeft = NULL;
        topRight = NULL;
        bottomLeft = NULL;
        bottomRight = NULL;
    }
    
    Node(bool _val, bool _isLeaf) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = NULL;
        topRight = NULL;
        bottomLeft = NULL;
        bottomRight = NULL;
    }
    
    Node(bool _val, bool _isLeaf, Node* _topLeft, Node* _topRight, Node* _bottomLeft, Node* _bottomRight) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = _topLeft;
        topRight = _topRight;
        bottomLeft = _bottomLeft;
        bottomRight = _bottomRight;
    }
};
*/

class Solution {
public:
    bool sameValue(std::vector<std::vector<int>> &grid, int x1, int y1, int size) {
        for (int i = x1; i < x1 + size; ++i) {
            for (int j = y1; j < y1 + size; ++j) {
                if (grid[i][j] != grid[x1][y1]) {
                    return false;
                }
            }
        }
        return true;
    }
    Node* dfs(std::vector<std::vector<int>> &grid, int x, int y, int size) {
        if (sameValue(grid, x, y, size)) {
            return new Node(grid[x][y], true);
        }
        Node* root = new Node(false, false);
        root -> topLeft = dfs(grid, x, y, size / 2);
        root -> topRight = dfs(grid, x, y + size / 2, size / 2);
        root -> bottomLeft = dfs(grid, x + size / 2, y, size / 2);
        root -> bottomRight = dfs(grid, x + size / 2, y + size / 2, size / 2);

        return root;

    }
    Node* construct(vector<vector<int>>& grid) {
        return dfs(grid, 0, 0, grid.size());
    }
};
