class Solution {
public:
    int pairSum(ListNode* head) {
        vector<int>sums;
        ListNode* s, *f;
        s = f = head;
        
        while (f && f->next) {
            sums.push_back(s->val);
            s = s->next;
            f = f->next->next;
        }
        
        int max = -1;

        for (int i = sums.size() - 1; i >= 0; i--) {
            sums[i] += s->val;
            s = s->next;
            if (sums[i] > max) max = sums[i];
        }

        return max;
    }
};