class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> hmap;
        vector<int> res;
        int toFind;

        for (int i = 0; i < nums.size(); i++) {
            toFind = target - nums[i];
            if (hmap.find(toFind) != hmap.end()) {
                res.push_back(hmap[toFind]);
                res.push_back(i);
                break;
            }
            hmap[nums[i]] = i;
        }
        return res;
    }
};