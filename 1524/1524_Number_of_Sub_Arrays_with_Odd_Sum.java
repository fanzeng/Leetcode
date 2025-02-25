class Solution {
    public int numOfSubarrays(int[] arr) {
        int res = 0;
        int prevOdd = 0;
        int prevEven = 1;
        int sum = 0;
        for (int i = 0; i < arr.length; i++) {
            sum += arr[i];
            if (sum % 2 == 0) {
                res += prevOdd;
                prevEven++;
            } else {
                res += prevEven;
                prevOdd++;
            }
            res %= 1e9+7;
        }
        return res;
    }
}
