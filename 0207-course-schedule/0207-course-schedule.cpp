class Solution {
public:

    bool dfs(vector<vector<int>>& adjs, int v, unordered_set<int>& visit, unordered_set<int>& path) {
        if (path.count(v) > 0) return false;
        if (visit.count(v) > 0) return true;
        

        visit.insert(v);
        path.insert(v);
        bool status = true;
        for (int i = 0; i < adjs[v].size(); i++) {
            if (!dfs(adjs, adjs[v][i], visit, path)) status = false;
        }
        path.erase(v);
        return status;

    }
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        
        vector<vector<int>>adjs(numCourses);
        unordered_set<int>visit;
        unordered_set<int>path;
        vector<int>res;
        for (int i = 0; i < numCourses; i++)
        {
            adjs[i] = vector<int>();
        }

        for (int i = 0; i < prerequisites.size(); i++) {
            int a = prerequisites[i][0], b = prerequisites[i][1];
            adjs[b].push_back(a);
        }

        for (int i = 0; i < numCourses; i++) {
            if (!dfs(adjs, i, visit, path)) return false;
        }

        if (visit.size() == numCourses) return true;
        return false;
    }
};