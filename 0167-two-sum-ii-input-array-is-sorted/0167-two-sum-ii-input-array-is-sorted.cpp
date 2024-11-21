class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l, r;
        l = 0, r = numbers.size() - 1;
        vector<int> res;

        while (l < r) {
            if (numbers[l] + numbers[r] == target) {
                res.push_back(l + 1);
                res.push_back(r + 1);
                break;
            }
            else if (numbers[l] + numbers[r] < target) l++;
            else r--;
        }
        return res;
    }
};