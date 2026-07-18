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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        int index = 0;
        std::unordered_map<int, int> umap;
        for (int i = 0; i < inorder.size(); ++i) {
            umap[inorder[i]] = i;
        } 
        std::function<TreeNode*(int, int)> build = [&](int left, int right) -> TreeNode* {
            if (left > right) {
                return nullptr;
            }
            TreeNode* node = new TreeNode(preorder[index]);
            int idx = umap[preorder[index++]];
            node->left = build(left, idx - 1);
            node->right = build(idx + 1, right);
            return node;
        };
        return build(0, preorder.size() - 1);
    }
};
