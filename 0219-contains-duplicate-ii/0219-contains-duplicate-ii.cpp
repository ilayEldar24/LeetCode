class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        int l = 0;
        unordered_set<int> hset;

        for (int r = 0; r < nums.size() ; r++){
            if (r - l > k) {
                hset.erase(nums[l]);
                l++;
            }
            if (hset.count(nums[r]) > 0) {
                return true;
            }
            hset.insert(nums[r]);
        }

        return false;

    }
};