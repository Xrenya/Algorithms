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
    int sumNumbers(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }
        int acc = 0;
        std::function<void(TreeNode*, int)> dfs = [&](TreeNode* node, int total) -> void {
            if (node->left == nullptr && node->right == nullptr) {
                acc += total * 10 + node->val;
                return;
            }
            total = total * 10 + node->val;
            if (node->left) dfs(node->left, total);
            if (node->right) dfs(node->right, total);
        };
        dfs(root, 0);
        return acc;
    }
};
