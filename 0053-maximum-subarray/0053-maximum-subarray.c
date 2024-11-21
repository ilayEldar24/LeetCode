int maxSubArray(int* nums, int numsSize) {
	int curSum, maxSum;
	maxSum = nums[0];
	curSum = 0;

	for (int i = 0; i < numsSize; i++){
		if (curSum<0) curSum = 0;
		curSum += nums[i];
		if(curSum > maxSum) maxSum= curSum;
	}
	
	return maxSum;

}