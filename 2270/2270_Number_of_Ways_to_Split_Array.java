class Solution {
    public int waysToSplitArray(int[] nums) {
        long total = 0;
        for (int num : nums) {
            total += num;
        }
        // System.out.println("total = " + total);
        long sum = 0;
        int count = 0;
        for (int i = 0; i < nums.length-1; i++) {
            sum += nums[i];
            if (sum >= total-sum) count++;
        }
        return count;
    }
}
