class Solution {
public:
    bool dfs(vector<vector<int>>& adjs, int v, unordered_set<int>& visited, vector<int>& topSort, unordered_set<int>& path) {
        if (path.count(v) > 0) return false;
        if (visited.count(v) > 0) return true;
        visited.insert(v);
        path.insert(v);
        bool status = true;
        for (int i = 0; i < adjs[v].size(); i++)
        {
            if (!dfs(adjs, adjs[v][i], visited, topSort, path)) status = false;
        }
        if (status)
        {
            topSort.push_back(v);
            path.erase(v);
            return true;
        }
        return false;
    }
    
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int>topSort;

        vector<vector<int>>adjs(numCourses);
        unordered_set<int>visited;
        unordered_set<int>path;
        for (int i = 0; i < numCourses; i++)
        {
            adjs[i] = vector<int>();
        }
        
        for (int i = 0; i < prerequisites.size(); i++) {
            int a = prerequisites[i][0], b = prerequisites[i][1];
            adjs[b].push_back(a);
        }

        for (int i = 0; i < numCourses; i++)
        {
            if (!dfs(adjs, i, visited, topSort, path)) return vector<int>();
        }

        if (visited.size() == numCourses) {
            reverse(topSort.begin(), topSort.end());
            return topSort;
        }
        return  vector<int>();

    }
};