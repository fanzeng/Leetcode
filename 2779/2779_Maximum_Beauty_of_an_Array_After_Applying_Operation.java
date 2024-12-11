class Solution {
    public int maximumBeauty(int[] nums, int k) {
        Arrays.sort(nums);
        int i = 0, j = 1;
        int ans = 1;
        while (j <= nums.length) {
            while (Math.abs(nums[j-1] - nums[i]) > 2*k) i++;
            ans = Math.max(ans, j-i);
            j++;
        }
        return ans;
    }
}
