class Solution {
    public int minimumSubarrayLength(int[] nums, int k) {
        int[] bors = new int[nums.length];
        int bor = nums[0];
        bors[0] = bor;
        for (int i = 1; i < nums.length; i++) {
            bor = bor | nums[i];
            bors[i] = bor;
        }
        if (bors[bors.length-1] < k) return -1;
        
        int[] counts = new int[32];
        int res = bors.length;
        int lower = 0, upper = 0; // Both inclusive
        while (upper < nums.length) {
            updateCounts(counts, nums[upper], 1);
            while (lower <= upper && getBorFromCounts(counts) >= k) {
                res = Math.min(res, upper - lower + 1);
                updateCounts(counts, nums[lower], -1);
                lower++;
            }
            upper++;
        }
        return res;
    }
    private void updateCounts(int[] counts, int num, int delta) {
        for (int b = 0; b < 32; b++) {
            if (((num >> b) & 1) != 0) {
                counts[b] += delta;
            }
        }
    }
    private int getBorFromCounts(int[] counts) {
        int bor = 0;
        for (int b = 0; b < 32; b++) {
            if (counts[b] > 0) {
                bor |= 1 << b;
            }
        }
        return bor;
    }
}
