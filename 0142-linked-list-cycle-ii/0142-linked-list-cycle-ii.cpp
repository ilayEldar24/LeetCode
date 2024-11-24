/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* detectCycle(ListNode* head) {
        ListNode* s, *f;
        s = f = head;
        bool found = false;
        ListNode* res = nullptr;

        while (f && f->next) {
            s = s->next;
            f = f->next->next;

            if (s == f) {
                found = true;
                break;
            }
        }
        
        if (!found) return res;

        ListNode* s2 = head;

        while (s != s2) {
            s = s->next;
            s2 = s2->next;
        }

        return s;
    
    }
};