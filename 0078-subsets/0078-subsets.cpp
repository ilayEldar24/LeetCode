using namespace std;

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int>curSet;
        vector<vector<int>>subSets;
        helper(nums, 0, curSet, subSets);
        return subSets;
    }

    void helper(vector<int>& nums, int i, vector<int>& curSet, vector<vector<int>>& subSets) {
        if (i >= nums.size()) {
            subSets.push_back(vector<int>(curSet));
            return;
        }
        
        curSet.push_back(nums[i]);
        helper(nums, i + 1, curSet, subSets);
        curSet.pop_back();



        helper(nums, i + 1, curSet, subSets);
    }
};
