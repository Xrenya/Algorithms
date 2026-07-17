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
    ListNode* dfs(ListNode* list1, ListNode* list2) {
        if (list1 != nullptr && list2 != nullptr) {
            ListNode * node;
            if (list1->val < list2->val) {
                node = new ListNode(list1->val);
                list1 = list1->next;
            } else {
                node = new ListNode(list2->val);
                list2 = list2->next;
            }
            node->next = dfs(list1, list2);
            return node;
        } else if ((list1 == nullptr && list2 != nullptr) || (list1 != nullptr && list2 == nullptr)) {
            ListNode * node;
            if (list1 == nullptr) {
                node = new ListNode(list2->val);
                node->next = dfs(list1, list2->next);
                return node;
            } else {
                node = new ListNode(list1->val);
                node->next = dfs(list1->next, list2);
                return node;
            }
        }
        return nullptr;
    }

    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if (list1 == nullptr && list2 == nullptr) {
            return nullptr;
        } else if (list2 == nullptr && list1 != nullptr) {
            return list1;
        } else if (list1 == nullptr && list2 != nullptr) {
            return list2;
        }
        ListNode * ptr;
        if (list1->val < list2->val) {
            ptr = list1;
            list1 = list1->next;
        } else {
            ptr = list2;
            list2 = list2->next;
        }
        ptr->next = mergeTwoLists(list1, list2);
        return ptr;
        // return dfs(list1, list2);
    }
};
