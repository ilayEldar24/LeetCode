int minSubArrayLen(int target, int* nums, int numsSize) {
	int len = INT_MAX;
	int L = 0, R = 0;
	int curSum = 0;
	
	for (R; R < numsSize; R++) {
		curSum += nums[R];
		while (curSum >= target && L <= R) {
			if (R - L + 1 < len) len = R - L + 1;
			curSum -= nums[L];
			L++;
		}
	}
    if (len!=INT_MAX) return len;
    else return 0;

}