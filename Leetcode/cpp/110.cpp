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

class Solution {
public:
    int recursive(TreeNode* root) {
        if (!root) {
            return 0;
        }
        return 1 + std::max(recursive(root->left), recursive(root->right));
    }
    bool isBalanced(TreeNode* root) {
        if (!root) {
            return true;
        }
        return (
            std::abs(recursive(root->left) - recursive(root->right)) <= 1
            && isBalanced(root->left)
            && isBalanced(root->right)
        );
    }
};
