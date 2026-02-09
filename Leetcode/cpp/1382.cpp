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
#include <iostream>
#include <vector>

class Solution {
public:
    std::vector<int> inorder;

    void inorder_traverse(TreeNode* node) {
        if (!node) return;
        inorder_traverse(node->left);
        inorder.push_back(node->val);
        inorder_traverse(node->right);
    }

    TreeNode* create_balance_bst(int start, int end) {
        if (start > end) return NULL;

        int mid = start + (end - start) / 2;
        TreeNode* node = new TreeNode(inorder[mid]);
        node->left = create_balance_bst(start, mid - 1);
        node->right = create_balance_bst(mid + 1, end);

        return node;
    }
    TreeNode* balanceBST(TreeNode* root) {
        inorder.clear();
        inorder_traverse(root);
        return create_balance_bst(0, inorder.size() - 1);
    }
};
