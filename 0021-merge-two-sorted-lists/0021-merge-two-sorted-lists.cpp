class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* head = nullptr, *cur = nullptr;
        if (list1 && list2) {
            if (list1->val > list2->val) {
                head = list2;
                list2 = list2->next;
            }
            else {
                head = list1;
                list1 = list1->next;
            }
            cur = head;

            while (list1 && list2) {
                if (list1->val > list2->val) {
                    cur->next = list2;
                    list2 = list2->next;
                }
                else {
                    cur->next = list1;
                    list1 = list1->next;
                }
                cur = cur->next;
            }

            while (list1) {
                cur->next = list1;
                list1 = list1->next;
                cur = cur->next;
            }

            while (list2) {
                cur->next = list2;
                list2 = list2->next;
                cur = cur->next;
            }

            return head;
        }
        else {
            if (list1) return list1;
            else if (list2) return list2;
            else return nullptr;
        }
    }
};