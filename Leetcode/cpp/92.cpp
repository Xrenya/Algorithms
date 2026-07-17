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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
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
};
