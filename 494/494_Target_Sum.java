class Solution {
    public int findTargetSumWays(int[] nums, int target) {
        int sum = Arrays.stream(nums).sum();
        if (Math.abs(target) > sum || (target + sum) % 2 != 0) return 0;
        int[][] memo = new int[nums.length][2*(Math.abs(target)+sum)+1];
        for (int i = 0; i < memo.length; i++) {
            for (int j = 0; j < memo[0].length; j++) {
                memo[i][j] = -1;
            }
        }
        return dp(nums, target, memo);
    }
    private int dp(int[] nums, int target, int[][] memo) {
        if (nums.length == 0) return target == 0 ? 1 : 0;
        int m = memo[nums.length-1][target + (memo[0].length-1)/2];
        if (m > 0) return m;
        int[] sub = Arrays.copyOfRange(nums, 1, nums.length);
        int pos = dp(sub, target-nums[0], memo);
        int neg = dp(sub, target+nums[0], memo);
        int res = pos + neg;
        memo[nums.length-1][target + (memo[0].length-1)/2] = res;
        return res;
    }
}
