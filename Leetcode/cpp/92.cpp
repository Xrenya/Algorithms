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
    ListNode* reverseBetweenDfs(ListNode* head, int left, int right) {
        if (head == nullptr) {
            return head;
        }

        bool stop = false;
        ListNode* leftNode = head;
        ListNode* rightNode = head;

        std::function<void(ListNode*, int, int)> backtrack = [&](ListNode* node, int leftIndex, int rightIndex) {
            if (rightIndex == 1) {
                return;
            }

            node = node->next;
            if (leftIndex > 1) {
                leftNode = leftNode->next;
            }
            backtrack(node, leftIndex - 1, rightIndex - 1);

            if (leftNode == node || node->next == leftNode) {
                stop = true;
                return;
            }

            if (!stop) {
                std::swap(leftNode->val, node->val);
                leftNode = leftNode->next;
            }
        };
        backtrack(rightNode, left, right);
        return head;
    }
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (head == nullptr || left == right) {
            return head;
        }
        ListNode * prev = nullptr;
        ListNode * dummy = new ListNode(0, head);
        ListNode * leftNode = dummy;
        for (int i = 0; i < left - 1; ++i) {
            leftNode = leftNode->next;
        }
        ListNode * tail = leftNode->next;
        ListNode * preLeft = leftNode;
        ListNode * cur = leftNode->next;
        for (int i = 0; i <= right - left; ++i) {
            ListNode * nextNode = cur->next;
            cur->next = prev;
            prev = cur;
            cur = nextNode;
        }
        preLeft->next = prev;
        tail->next = cur;
        ListNode * returnNode = dummy->next;
        delete dummy;
        return returnNode;

    }
};
