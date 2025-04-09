class Solution {
    public int minOperations(int[] nums, int k) {
        int res = 0;
        int[] counts = new int[101];
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] < k) return -1;
            if (nums[i] > k && counts[nums[i]]++ == 0) res++;
        }
        return res;
    }
}
