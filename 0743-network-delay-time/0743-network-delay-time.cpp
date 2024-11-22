class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        // Min-heap: {distance, node}
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minHeap;
        unordered_map<int, int> shortests;

        // Adjacency list: node -> {destination, weight}
        unordered_map<int, vector<pair<int, int>>> adjs;
        for (int i = 1; i <= n; i++) {
            adjs[i] = vector<pair<int, int>>();
        }

        // Fill adjacency list
        for (vector<int>& time : times) {
            int src = time[0];
            int dest = time[1];
            int w = time[2];
            adjs[src].push_back(make_pair(dest, w));
        }

        // Start Dijkstra's algorithm from node k
        minHeap.push({0, k}); // {distance, node}

        while (!minHeap.empty()) {
            auto [w1, v1] = minHeap.top();
            minHeap.pop();
            if (shortests.count(v1) > 0) continue;
            shortests[v1] = w1;

            for (pair<int, int>& curPair : adjs[v1]) {
                int v2 = curPair.first, w2 = curPair.second;
                if (shortests.count(v2) == 0) {
                    minHeap.push({w1 + w2, v2});
                }
            }
        }

        // If not all nodes are reached, return -1
        if (shortests.size() < n) return -1;

        // Find the maximum time
        int maxTime = 0;
        for (const auto& [node, time] : shortests) {
            maxTime = max(maxTime, time);
        }

        return maxTime;
    }
};
