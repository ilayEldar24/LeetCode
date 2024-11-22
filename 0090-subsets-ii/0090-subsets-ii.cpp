
class Solution {
public:

    void helper(vector<int>& nums, int i, vector<int>&curSet, vector<vector<int>>&subSets) {
        if (i >= nums.size()) {
            subSets.push_back(vector<int>(curSet));
            return;
        }
        
        curSet.push_back(nums[i]);
        helper(nums, i + 1, curSet, subSets);
        curSet.pop_back();


        while (i + 1 < nums.size() && nums[i] == nums[i + 1]) {
            i++;
        }
        helper(nums, i + 1, curSet, subSets);
    }

    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<int> curSet;
        vector<vector<int>> subSets;
        helper(nums, 0, curSet, subSets);
        return subSets;


    }
};
