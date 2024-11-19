class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        
        int k = 0;
        
        for(int r=0;r<nums.size();r++){
            if(nums.at(r) != val){
                nums[k] = nums.at(r);
                k+=1;
            }
        }
        
        return k;
        
        
        
    }
};