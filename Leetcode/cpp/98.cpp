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
    bool isValidBST(TreeNode* root) {
        if (root == nullptr || (root->left == nullptr && root->right == nullptr)) {
            return true;
        }
        std::function<bool(TreeNode*, long long, long long)> dfs = [&](TreeNode* node, long long left, long long right) -> bool {
            if (node == nullptr) {
                return true;
            }
            if (left >= node->val || node->val >= right) {
                return false;
            }
            return dfs(node->left, left, node->val) && dfs(node->right, node->val, right);
        };
        return dfs(root, LLONG_MIN, LLONG_MAX);
    }
};
