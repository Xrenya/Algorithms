class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (head == nullptr || head->next == nullptr) {
            return head;
        }

        ListNode* prev = new ListNode(-101, head);
        ListNode* cur = head;
        ListNode* dummy = prev;
        
        while (cur != nullptr) {
            if (cur->next && cur->val == cur->next->val) {
                while (cur->next && cur->val == cur->next->val) {
                    cur = cur->next;
                }
                prev->next = cur->next;
            } else {
                prev = prev->next;
            }

            cur = cur->next;
        }
        ListNode* returnHead = dummy->next;
        delete dummy;
        return returnHead;
    }

    ListNode* deleteDuplicatesGood(ListNode* head) {
        ListNode dummy(0, head);
        ListNode* prev = &dummy;

        while (prev->next != nullptr) {
            ListNode* cur = prev->next;
            bool duplicate = false;

            // Find the end of the duplicate group.
            while (cur->next != nullptr &&
                   cur->val == cur->next->val) {
                duplicate = true;

                ListNode* toDelete = cur;
                cur = cur->next;
                delete toDelete;
            }

            if (duplicate) {
                // Delete the final node in the duplicate group too.
                ListNode* toDelete = cur;
                cur = cur->next;
                delete toDelete;

                // Skip the entire duplicate group.
                prev->next = cur;
            } else {
                // This node is unique.
                prev = prev->next;
            }
        }

        return dummy.next;
    }
};
