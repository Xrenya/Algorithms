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
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        int n = inorder.size();
        int index = n - 1;
        std::unordered_map<int, int> umap;
        for (int i = 0; i < n; ++i) {
            umap[inorder[i]] = i;
        }
        std::function<TreeNode*(int, int)> build = [&](int left, int right) -> TreeNode* {
            if (left > right) {
                return nullptr;
            }
            TreeNode* node = new TreeNode(postorder[index]);
            int idx = umap[postorder[index--]];
            node->right = build(idx + 1, right);
            node->left = build(left, idx - 1);
            return node;
        };
        return build(0, n - 1);
    }
};
