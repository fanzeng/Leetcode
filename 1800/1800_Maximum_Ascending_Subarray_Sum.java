class Solution {
    public int maxAscendingSum(int[] nums) {
        int maxSum = nums[0];
        int s = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > nums[i-1]) {
                s += nums[i];
                if (s > maxSum) maxSum = s;
            } else {
                s = nums[i];
            }
        }
        return maxSum;
    }
}
