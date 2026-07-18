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
    TreeNode* dfs(TreeNode* root) {
        if (root == nullptr) {
            return root;
        }
        if (root->left == nullptr || root->right == nullptr) {
            return root;
        }
        TreeNode * left = dfs(root->left);
        TreeNode * right = dfs(root->right);
        if (left) {
            left->right = root->right;
            root->right = root->left;
            root->left = nullptr;
        }
        return right ? right : left;
    }
    void flatten(TreeNode* root) {
        dfs(root);
    }
};
