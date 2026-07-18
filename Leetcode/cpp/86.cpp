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
    ListNode* partition(ListNode* head, int x) {
        if (head == nullptr || head->next == nullptr) {
            return head;
        }

        ListNode * tail = new ListNode(-201, head);
        ListNode * prev = tail;
        ListNode * returnHead = tail;
        int counter = 0;
        while (tail != nullptr && tail->next != nullptr) {
            ++counter;
            tail = tail->next;
        }

        ListNode * cur = head;
        for (int i = 0; i < counter; ++i) {
            if (cur == tail) break;
            if (cur->val >= x) {
                ListNode * nextNode = cur->next;
                prev->next = nextNode;
                tail->next = cur;
                cur->next = nullptr;
                cur = nextNode;
                tail = tail->next;
            } else {
                cur = cur->next;
                prev = prev->next;
            }
        }
        ListNode* res = returnHead->next;
        delete returnHead;
        return res;
    }
};

