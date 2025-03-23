class Solution {
    public int longestNiceSubarray(int[] nums) {
        int i = 0, j = 0;
        int ans = 1;
        while (++j < nums.length) {
            int k = j;
            while (--k >= i) {
                // System.out.printf("%d & %d = %d\n", nums[k], nums[j], nums[k] & nums[j]);
                if ((nums[k] & nums[j]) > 0) {
                    i = k+1;
                    break;
                }
            }
            ans = Math.max(ans, j-k);
        }
        return ans;
    }
}
