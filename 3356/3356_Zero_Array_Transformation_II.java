class Solution {
    public int minZeroArray(int[] nums, int[][] queries) {
        if (Arrays.stream(nums).sum() == 0) return 0;
        return binarySearch(nums, queries) + 1;
    }
    private int[] getDiff(int[][] queries, int n, int k) {
        int[] diff = new int[n+1];
        for (int i = 0; i <= k; i++) {
            int[] q = queries[i];
            diff[q[0]] += q[2];
            diff[q[1]+1] -= q[2];
        }
        return diff;
    }
    // Given the diff of the array of the cumulative q[2] sum over first k queries,
    // decide if it's enough to zero all n in nums.
    // diff[i] of an array arr is the difference between arr[i+1] and arr[i].
    private boolean canZero(int[] nums, int[] diff) {
        int s = 0;
        for (int i = 0; i < nums.length; i++) {
            s += diff[i];
            if (nums[i] > s) return false;
        }
        return true;
    }
    private int binarySearch(int[] nums, int[][] queries) {
        int l = 0;
        int r = queries.length;
        // Find the smallest index that canZero.
        while (l < r) {
            int m = (l + r)/2;
            if (canZero(nums, getDiff(queries, nums.length, m))) {
                r = m;
            } else {
                l = m+1;
            }
        }
        if (l == queries.length) return -2;
        return l;
    }
}
