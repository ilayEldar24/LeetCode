class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int size = nums.size();
        vector<int> res(size, 1);
        int pre = 1;

        for (int i = 0; i < size; i++)
        {
            res[i] *= pre;
            pre *= nums[i];
        }

        int suf = 1;

        for (int i = size-1;i >= 0;i--)
        {
            res[i] *= suf;
            suf *= nums[i];
        }

        return res;

    }
};