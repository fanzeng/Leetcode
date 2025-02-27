class Solution {
    public int lenLongestFibSubseq(int[] arr) {
        return dp(arr, 0, -1, -1);
    }
    private int dp(int[] arr, int start, int a, int b) {
        if (arr.length <= start) return 0;
        int res = 0;
        if (a == -1) {
            for (int i = start; i < arr.length; i++) {
                a = arr[i];
                int sub = dp(arr, i+1, a, -1);
                res = Math.max(sub, res);
            }
            if (res == 0) return 0;
        } else if (b == -1) {
            for (int i = start; i < arr.length; i++) {
                b = arr[i];
                int sub = dp(arr, i+1, a, b);
                res = Math.max(sub, res);
            }
            if (res == 0) return 0;
        } else {
            boolean found = false;
            for (int i = start; i < arr.length; i++) {
                if (arr[i] == a + b) {
                    found = true;
                    a = b;
                    b = arr[i];
                    res = dp(arr, i+1, a, b);
                    break;
                }
            }
            return found ? res + 1 : 0;
        }
        return res + 1;
    }
}
