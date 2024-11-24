class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freqs;
        priority_queue<pair<int, int>>maxHeap;
        vector<int>res;

        for (int num : nums) {
            freqs[num] += 1;
        }

        for (auto& pair : freqs) {
            maxHeap.push({ pair.second, pair.first });
        }

        for (int i = 0; i < k; i++) {
            res.push_back(maxHeap.top().second);
            maxHeap.pop();
        }

        return res;
    }
};