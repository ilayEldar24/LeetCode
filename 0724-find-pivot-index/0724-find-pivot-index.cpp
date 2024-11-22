class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int size = nums.size();
        vector<int> prefix(size);
        vector<int> postfix(size);
        int res = -1;
        prefix[0] = nums[0];
        postfix[size - 1] = nums[size - 1];

        for (int i = 1; i < size; i++)
        {
            prefix[i] = prefix[i - 1] + nums[i];
            postfix[size - 1 - i] = postfix[size - i] + nums[size - i - 1];
        }

        for (int i = 0; i < size; i++) {
            if (prefix[i] == postfix[i]) return i;
        }

        return res;
    }
};