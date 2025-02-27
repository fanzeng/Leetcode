class Solution {
    public int maxAbsoluteSum(int[] nums) {
        int[] negativeNums = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            negativeNums[i] = - nums[i];
        }
        return Math.max(kadane(nums), kadane(negativeNums));
    }
    public int kadane(int[] nums) {
        int res = Integer.MIN_VALUE;
        int prefixSum = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i == 0 || nums[i] > prefixSum + nums[i]) {
                prefixSum = nums[i];
            } else {
                prefixSum += nums[i];
            }
            res = Math.max(prefixSum, res);
        }
        return res;
    }
}
