class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 1) return nums[0];
        if (nums.size() == 2) {
            if (nums[0] < nums[1]) {
                return nums[1];
            }
            else {
                return nums[0];
            }
        }

        int arr[2];
        arr[0] = nums[0];
        arr[1] = max(nums[0], nums[1]);
        int i = 2;

        while (i < nums.size()) {
            int tmp = arr[1];
            arr[1] = max(arr[0] + nums[i], arr[1]);
            arr[0] = tmp;
            i++;
        }

        return arr[1];
    }
};