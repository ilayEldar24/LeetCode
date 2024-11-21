int numOfSubarrays(int* arr, int arrSize, int k, int threshold) {
	int curSum=0, counter = 0, L = 0, R, curAvg;

	for (R = 0; R < k; R++)
	{
		curSum += arr[R];
	}
	
	curAvg = curSum / k;
	if (curAvg >= threshold) counter++;

	for (R; R < arrSize; R++) {
		curSum -= arr[L];
		L++;
		curSum += arr[R];
		curAvg = curSum / k;
		if (curAvg >= threshold) counter++;
	}

	return counter;
}
