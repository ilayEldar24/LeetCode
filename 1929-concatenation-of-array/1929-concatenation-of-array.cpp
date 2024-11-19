#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int size = nums.size() * 2;
        vector<int> ans;
        for (int i = 0; i < nums.size() * 2; i++) {
            ans.push_back(nums[i % nums.size()]);
        }
        return ans;
    }
};