class Solution {
public:
    int climbStairs(int n) {
        if (n <= 2) {
            return n;
        }

        int arr[2];
        int i = 2;
        
        arr[0] = 1;
        arr[1] = 2;

        while (i < n) {
            int tmp = arr[1];
            arr[1] = arr[0] + arr[1];
            arr[0] = tmp;
            i++;
        }

        return arr[1];
    }
};