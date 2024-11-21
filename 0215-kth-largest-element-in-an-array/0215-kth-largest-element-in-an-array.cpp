class Solution {
public:
    int partition(vector<int>& nums, int left, int right) {
        int mid = (left + right) >> 1;
        swap(nums[mid], nums[left + 1]);
        
        if (nums[left] < nums[right]) 
            swap(nums[left], nums[right]);
        if (nums[left + 1] < nums[right]) 
            swap(nums[left + 1], nums[right]);
        if (nums[left] < nums[left + 1]) 
            swap(nums[left], nums[left + 1]);
        
        int pivot = nums[left + 1];
        int i = left + 1;
        int j = right;
        
        while (true) {
            while (nums[++i] > pivot);
            while (nums[--j] < pivot);
            if (i > j) break;
            swap(nums[i], nums[j]);
        }
        
        nums[left + 1] = nums[j];
        nums[j] = pivot;
        return j;
    }
    
    int quickSelect(vector<int>& nums, int k) {
        int left = 0;
        int right = nums.size() - 1;
        
        while (true) {
            if (right <= left + 1) {
                if (right == left + 1 && nums[right] > nums[left])
                    swap(nums[left], nums[right]);
                return nums[k];
            }
            
            int j = partition(nums, left, right);
            
            if (j >= k) right = j - 1;
            if (j <= k) left = j + 1;
        }
    }
    
    int findKthLargest(vector<int>& nums, int k) {
        return quickSelect(nums, k - 1);
    }
};