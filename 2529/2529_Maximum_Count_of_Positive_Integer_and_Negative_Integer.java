class Solution {
    public int maximumCount(int[] nums) {
        int l = 0, r = nums.length;
        while (l < r) {
            int m = (l + r) / 2;
            if (nums[m] >= 0) {
                r = m;
            } else {
                l = m+1;
            }
        }
        int nCount = r;
        while (r < nums.length && nums[r] == 0) r++;
        return Math.max(nCount, nums.length - r);
    }
}
