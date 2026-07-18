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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* dummy = new ListNode(0, head);
        ListNode* slow = dummy, * fast = dummy;
        for (int i = 0; i < n; ++i) {
            fast = fast->next;
        }
        ListNode* prev = nullptr;
        while (fast != nullptr) {
            fast = fast->next;
            prev = slow;
            slow = slow->next;
        }
        ListNode* nextNode = (slow->next) ? slow->next : nullptr;

        prev->next = nextNode;
        delete slow;
        return dummy->next;
    }
};
