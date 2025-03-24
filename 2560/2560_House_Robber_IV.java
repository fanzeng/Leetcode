class Solution {
    public int minCapability(int[] nums, int k) {
        int l = 0;
        int max = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > max) {
                max = nums[i];
            }
        }
        // System.out.printf("max = %d\n", max);
        int r = max+1;
        while (l < r) {
            int m = (l + r) / 2;
            // System.out.printf("m = %d\n", m);
            if (canRob(nums, k, m)) {
                r = m;
            } else {
                l = m+1;
            }
        }
        return r;
    }
    // Check if possible to find k nonconsecutive houses with max of m.
    private boolean canRob(int[] nums, int k, int m) {
        int count = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] <= m) {
                count++;
                if (count == k) return true;
                i++;
            }
        }
        return false;
    }
}
