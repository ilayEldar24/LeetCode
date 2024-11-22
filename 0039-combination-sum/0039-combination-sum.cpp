class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> combs;
        vector<int> cur;
        helper(candidates, target, combs, cur, 0,0);
        return combs;
    }

    void helper(vector<int>& candidates, int target, vector<vector<int>>& combs, vector<int>& cur, int i, int curSum) {
        if (curSum > target) return;
        if (i == candidates.size()) return;
        if (curSum == target) {
            combs.push_back(vector<int>(cur));
            return;
        }

        cur.push_back(candidates[i%candidates.size()]);
        helper(candidates, target, combs, cur, i, curSum + candidates[i % candidates.size()]);

        cur.pop_back();

        helper(candidates, target, combs, cur, i + 1, curSum);
      
    }
};