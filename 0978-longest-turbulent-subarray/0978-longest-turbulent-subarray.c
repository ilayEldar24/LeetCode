
int maxTurbulenceSize(int* arr, int arrSize) {
	
	int curMax = 1 , globalMax = 1;
	
	if (arrSize == 1) {
		return 1;
	}


	if (arr[1] == arr[0]) {
		curMax = globalMax = 1;
	}
	else {
		curMax = globalMax = 2;
	}


	for (int i = 2; i < arrSize; i++)
	{
		if (arr[i] < arr[i - 1]) {
			if (arr[i - 1] > arr[i - 2]) {
				curMax++;
			}
			else {
				curMax = 2;
			}
		}
		else if (arr[i] > arr[i - 1]) {
			if (arr[i - 1] < arr[i - 2]) {
				curMax++;
			}
			else {
				curMax = 2;
			}
		}
		else curMax = 1;

		if (curMax > globalMax) globalMax = curMax;
	}

	return globalMax;

}