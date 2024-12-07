class Solution {
    public int minimumSize(int[] nums, int maxOperations) {
        int maxBags = nums.length + maxOperations;
        int l = 1;
        Arrays.sort(nums);
        int[] desc = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            desc[nums.length-1-i] = nums[i];
        }
        int r = desc[0];
        return binarySearch(l, r, desc, maxBags);
    }
    private boolean isFeasible(int[] nums, int minBall, int maxBags) {
        int count = 0;
        for (int i = 0; i < nums.length; i++) {
            int n = nums[i];
            count += Math.ceil(n*1. / minBall);
            if (count > maxBags) return false;
        }
        return true;
    }
    private int binarySearch(int l, int r, int[] nums, int maxBags) {
        while (l < r) {
            int m = (l + r) / 2;
            if (isFeasible(nums, m, maxBags)) {
                r = m;
            } else {
                l = m + 1;
            }
        }
        return l;
    }
}
