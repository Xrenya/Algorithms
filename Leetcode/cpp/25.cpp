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
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (head == nullptr || k <= 1) {
            return head;
        }

        ListNode* cur = head;

        for (int i = 0; i < k; ++i) {
            if (cur == nullptr) {
                return head;
            }
            cur = cur->next;
        }

        ListNode* nextGroup = cur;

        ListNode* prev = nullptr;
        cur = head;

        for (int i = 0; i < k; ++i) {
            ListNode* next = cur->next;
            cur->next = prev;
            prev = cur;
            cur = next;
        }

        head->next = reverseKGroup(nextGroup, k);

        return prev;
    }
};
