class Solution {
    public long countSubarrays(int[] nums, int k) {
        int max = -1;
        for (int i = 0; i < nums.length; i++) {
            if (max < nums[i]) max = nums[i];
        }
        long res = 0;
        int l = 0;
        int r = 0;
        int count = 0;
        while (r < nums.length) {
            while (count < k) {
                if (nums[r] == max) {
                    count++;
                    break;
                }
                if (++r == nums.length) break;
            }
            while (count == k) {
                res += nums.length - r;
                if (nums[l++] == max) {
                    count--;
                }
            }
            r++;
        }
        return res;
    }
}
