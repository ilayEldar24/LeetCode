class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
         vector<int> curComb;
        vector<vector<int>> combs;
        helper(n,k, 1, curComb, combs);
        return combs;
    }
    
    void helper(int n, int k, int i, vector<int>& curComb, vector<vector<int>>& combs) {
        if (curComb.size() == k) {
            combs.push_back(curComb);
            return;
        }
        if (i > n) return;

        curComb.push_back(i);
        helper(n, k, i + 1, curComb, combs);
        

        curComb.pop_back();
        helper(n, k, i + 1, curComb, combs);
    }
};