/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int getMinimumDifference(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }
        int value = 1000000;
        int leftNode = -1000000;
        int rightNode = 1000000;
        std::function<void(TreeNode*, int, int)> dfs = [&](TreeNode* node, int left, int right) -> void {
            if (node == nullptr) {
                return;
            }
            int tmp = std::min<int>(right - node->val, node->val - left);
            value = std::min<int>(value, tmp);
            if (node->left) dfs(node->left, left, node->val);
            if (node->right) dfs(node->right, node->val, right);
            return;
        };
        dfs(root, leftNode, rightNode);
        return value;
    }
};
