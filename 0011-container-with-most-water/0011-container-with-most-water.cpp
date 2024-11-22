class Solution {
public:
    int maxArea(vector<int>& height) {
        int cur = 0, max = 0;
        int l = 0, r = height.size() - 1;

        while (l < r) {
            height[l] > height[r] ? cur = height[r] * (r - l ) : cur = height[l] * (r - l );
            if (cur > max) max = cur;
            height[l] > height[r] ? r-- : l++;
        }

        return max;

    }
};