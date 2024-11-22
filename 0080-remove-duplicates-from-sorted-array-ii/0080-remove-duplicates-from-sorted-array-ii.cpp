class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int l = 0, r = 0, count;

        while (r < nums.size()) {
            count = 1;
            while (r + 1 < nums.size() && nums[r] == nums[r + 1]) {
                r++;
                count += 1;
            }

            if (count > 2) count = 2;

            for (int i = 0; i < count; i++)
            {
                nums[l] = nums[r];
                l++;
            }

            r++;
        }

        return l;
    };
};