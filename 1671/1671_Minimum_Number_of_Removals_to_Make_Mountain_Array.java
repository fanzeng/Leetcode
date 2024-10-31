class Solution {
    public int minimumMountainRemovals(int[] nums) {
        int[] lisLR = lis(nums);
        int[] rev = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            rev[i] = nums[nums.length-1-i];
        }
        int[] lisRL = lis(rev);
        int res = nums.length;
        for (int i = 1; i < nums.length-1; i++) {
            int lr = lisLR[i];
            int rl = lisRL[nums.length-1-i];
            // System.out.printf("i:%d, LR: %d, RL: %d\n", i, lr, rl);
            // We need at least 2 numbers including the peak to be valid.
            if (lr <= 1 || rl <= 1) continue;
            int ans = nums.length - (lr + rl - 1);
            if (ans < res) res = ans;
        }
        return res;
    }
    // Returns lengths of lis at each index
    private int[] lis(int[] nums) {
        int[] res = new int[nums.length];
        int[] lis = new int[nums.length];
        res[0] = 1;
        lis[0] = nums[0];
        int length = 1;
        for (int i = 1; i < nums.length; i++) {
            int n = nums[i];
            if (n > lis[length-1]) {
                lis[length++] = n;
                res[i] = length;
            } else if (n == lis[length-1]) {
                res[i] = length;
            }
            else {
                int j = binarySearch(lis, -1, length-1, n);
                lis[j] = n;
                // Whenever we read this res[i] result,
                // we're assuming the ith number is the peak.
                // So for this particular problem,
                // if we end up here, we know res[i] is not the peak,
                // and we need to make res[i] invalid.
                // Here we do not update res[i], so it's left at default value of 0.
            }
        }
        return res;
    }
    private int binarySearch(int[] arr, int l, int r, int n) {
        while (r - l > 1) {
            int m = (l + r) / 2;
            if (arr[m] >= n) {
                r = m;
            } else {
                l = m;
            }
        }
        return r;
    }
}
