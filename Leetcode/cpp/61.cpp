
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
    ListNode* rotateRight(ListNode* head, int k) {
    if (k == 0 || head == NULL || head->next == NULL) {
      return head;
    }
    ListNode* node = head;
    ListNode* tail;
    int length = 0;
    while (node != NULL) {
      tail = node;
      node = node->next;
      ++length;
    }
    tail->next = head;
    k = k % length;
    k = length - k;
    node = head;
    for (int i = 0; i < k - 1; ++i) {
        node = node->next;
    }
    ListNode* new_head = node->next;
    if (tail != NULL) {
      tail->next = head;
    }
    node->next = nullptr;
    return new_head;
    }
};
