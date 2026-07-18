
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
class SolutionV2 {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (k == 0 || head == nullptr) {
            return head;
        }
        int counter = 0;
        ListNode* tmp = head;
        while (tmp) {
            tmp = tmp->next;
            ++counter;
        }
        k %= counter;
        ListNode dummy = ListNode(0, head);
        ListNode* prev = &dummy;
        ListNode* cur = prev;
        for (int i = 0; i < k; ++i) {
            cur = cur->next;
        }

        while (cur != nullptr && cur->next != nullptr) {
            cur = cur->next;
            prev = prev->next;
        }
        
        cur->next = dummy.next;
        ListNode * tail = prev->next;
        prev->next = nullptr;
        return tail;
    }
};
