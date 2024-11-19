int removeElement(int* nums, int numsSize, int val) {

    int k = 0;

    for (int r = 0; r < numsSize; r++) {
        if (nums[r] != val) {
            nums[k] = nums[r];
            k += 1;
        }
    }
    return k;
    
}