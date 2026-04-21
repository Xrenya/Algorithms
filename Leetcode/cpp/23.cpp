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
    ListNode* merge(ListNode* left, ListNode* right) {
        ListNode dummy;
        ListNode* tail = &dummy;
        while (left && right) {
            if (left->val < right->val) {
                tail->next = left;
                left = left->next;
            } else {
                tail->next = right;
                right = right->next;
            }
            tail = tail->next;
        }
        tail->next = left ? left : right;
        return dummy.next;
    }

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        int size = lists.size();
        if (size == 0) return nullptr;

        int interval = 1;
        while (interval < size) {
            for (int i = 0; i < size - interval; i += interval * 2) {
                lists[i] = merge(lists[i], lists[i + interval]);
            }
            interval *= 2;
        }
        return lists[0];
    }
};
