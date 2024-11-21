class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> pq(stones.begin(), stones.end());
        int s1, s2;
        while (pq.size() > 1) {
            s1 = pq.top();
            pq.pop();
            s2 = pq.top();
            pq.pop();

            if (s1 != s2) {
                if (s1 > s2)  pq.push(s1 - s2);
                else pq.push(s2 - s1);
            }
        }
        if (pq.empty()) return 0;
        else return pq.top();
    }
};