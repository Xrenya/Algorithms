/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:

    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        return dfs(l1, l2, 0);
    }

    ListNode* dfs(ListNode* l1, ListNode* l2, int carry) {
        if (l1 == nullptr && l2 == nullptr && carry == 0) {
            return nullptr;
        }
        int l1Val = l1 ? l1->val : 0;
        int l2Val = l2 ? l2->val : 0;
        int value = l1Val + l2Val + carry;

        ListNode * node = new ListNode(value % 10);
        value /= 10;
        node->next = dfs(l1 ? l1->next : nullptr, l2 ? l2->next : nullptr, value);
        return node;
    }
};
