#include <iostream>
#include <vector>
#include <cassert>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    TreeNode* dfs(int left, int right, const std::vector<int>& nums) {
        if (left > right) return nullptr;

        int mid = left + (right - left) / 2;
        TreeNode* root = new TreeNode(nums[mid]);

        root->left  = dfs(left, mid - 1, nums);
        root->right = dfs(mid + 1, right, nums);

        return root;
    }

    TreeNode* sortedArrayToBST(std::vector<int>& nums) {
        if (nums.empty()) return nullptr;
        return dfs(0, (int)nums.size() - 1, nums);
    }
};

// Helper function to check if two trees are structurally identical
bool isSameTree(TreeNode* p, TreeNode* q) {
    if (p == nullptr && q == nullptr) return true;
    if (p == nullptr || q == nullptr) return false;
    if (p->val != q->val) return false;
    
    return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
}

// Helper function to free allocated memory
void deleteTree(TreeNode* root) {
    if (root == nullptr) return;
    deleteTree(root->left);
    deleteTree(root->right);
    delete root;
}

int main() {
    Solution sol;
    std::vector<int> nums = {-10, -3, 0, 5, 9};

    /* 
       Trace your algorithm to build the EXACT expected tree:
       dfs(0, 4) -> mid=2 (val 0)
         left: dfs(0, 1) -> mid=0 (val -10)
            right: dfs(1, 1) -> mid=1 (val -3)
         right: dfs(3, 4) -> mid=3 (val 5)
            right: dfs(4, 4) -> mid=4 (val 9)
    */

    // Use 'new' to allocate pointers properly
    TreeNode* expected_tree = new TreeNode(0);
    expected_tree->left = new TreeNode(-10);
    expected_tree->left->right = new TreeNode(-3); // Right child due to integer division
    expected_tree->right = new TreeNode(5);
    expected_tree->right->right = new TreeNode(9); // Right child due to integer division

    // Pass 'nums' to the function
    TreeNode* output = sol.sortedArrayToBST(nums);

    // Use the helper function to compare the two trees deeply
    assert(isSameTree(expected_tree, output) && "Test #1 failed!");
    
    std::cout << "All tests passed!" << std::endl;

    // Clean up memory
    deleteTree(expected_tree);
    deleteTree(output);

    return 0;
}
