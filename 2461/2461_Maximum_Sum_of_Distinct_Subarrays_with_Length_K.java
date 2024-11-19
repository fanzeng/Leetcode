class Solution {
    public long maximumSubarraySum(int[] nums, int k) {
        long maxSum = 0;
        long sum = 0;
        HashMap<Integer, Integer> hm = new HashMap<>(); // Count of number in subarray
        for (int i = 0; i < k; i++) {
            sum += nums[i];
            int count = hm.getOrDefault(nums[i], 0);
            hm.put(nums[i], count + 1);
        }
        boolean qualified = qualify(nums, 0, k, hm);
        if (qualified) maxSum = sum;
        int i = 1;
        int j = i+k-1;
        while (j < nums.length) {
            sum += nums[j] - nums[i-1];
            int count = hm.get(nums[i-1]);
            hm.put(nums[i-1], count - 1);
            count = hm.getOrDefault(nums[j], 0);
            hm.put(nums[j], count + 1);
            if (qualified) {
                qualified = qualifyNewAdded(nums, j, hm);
            } else {
                qualified = qualify(nums, i, j+1, hm);
            }
            if (qualified && sum > maxSum) maxSum = sum;
            i++;
            j++;
        }
        return maxSum;
    }
    // i inclusive, j exclusive
    private boolean qualify(int[] nums, int i, int j, HashMap<Integer, Integer> hm) {
        for (int k = i; k < j; k++) {
            if (hm.getOrDefault(nums[k], 0) > 1) return false;
        }
        return true;
    }
    // k is the index of the newly added element
    private boolean qualifyNewAdded(int[] nums, int k, HashMap<Integer, Integer> hm) {
        return hm.getOrDefault(nums[k], 0) <= 1;
    }
}
