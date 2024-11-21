int removeDuplicates(int* nums, int numsSize) {
	int p = 1, r = 1;
	for (r; r < numsSize; r++){
		if (nums[p] > nums[p - 1]) p++;
		else {
			if (nums[r] > nums[r - 1]) {
				nums[p] = nums[r];
				p++;
			}
		}

	}
    return p;
}
