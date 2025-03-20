class Solution {
    public int minOperations(int[] nums) {
        if (nums.length < 3) return -1;
        return operate(nums, 0);
    }
    private int operate(int[] nums, int i) {
        if (nums.length-i == 3) {
            if (nums[i] == nums[i+1] && nums[i+1] == nums[i+2]) {
                return 1 - nums[i];
            } else {
                return -1;
            }
        }
        if (nums[i] == 0) {
            nums[i+1] = 1 - nums[i+1];
            nums[i+2] = 1 - nums[i+2];
            int next = operate(nums, i+1);
            return next == -1 ? next : next + 1;
        }
        return operate(nums, i+1);
    }
}
