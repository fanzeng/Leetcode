class Solution {
    public int[] buildArray(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            nums[i] += (nums[nums[i]] % 1000) * 1000;
        }
        for (int i = 0; i < nums.length; i++) {
            nums[i] /= 1000;
        }
        return nums;
    }
}
