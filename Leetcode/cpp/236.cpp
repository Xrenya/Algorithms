/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        TreeNode* output;
        std::function<int(TreeNode*)> dfs = [&](TreeNode* node) -> int {
            if (node == nullptr) {
                return 0;
            }
            int left = dfs(node->left);
            int right = dfs(node->right);
            int res = (node == q) || (node == p);
            if (res + left + right >= 2) {
                output = node;
            }
            return res || left || right;
        };
        dfs(root);
        return output;
    }
};
