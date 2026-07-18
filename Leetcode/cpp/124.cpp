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
    int maxPathSum(TreeNode* root) {
        int maxValue = INT_MIN;
        std::function<int(TreeNode*)> dfs = [&](TreeNode* node) -> int {
            if (node == nullptr) {
                return 0;
            }
            int left = std::max<int>(dfs(node->left), 0);
            int right = std::max<int>(dfs(node->right), 0);
            maxValue = std::max<int>(maxValue, left + right + node->val);
            return node->val + std::max<int>(left, right);
        };
        dfs(root);
        return maxValue;
    }
};
