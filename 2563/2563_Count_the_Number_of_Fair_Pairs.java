class Solution {
    public long countFairPairs(int[] nums, int lower, int upper) {
        Arrays.sort(nums);
        // System.out.println(Arrays.toString(nums));
        int i = 0;
        long count = 0;
        int k = nums.length - 1;
        while (i < nums.length - 1) {
            // System.out.printf("nums[%d] = %d\n", i, nums[i]);
            // Find the first j such that nums[i] + nums[j] >= lower
            int j = firstGeq(nums, i+1, nums.length, lower - nums[i]);
            // Find the last k such that nums[i] + nums[k] <= upper
            if (j <= k && nums[i] + nums[j] <= upper) {
                k = lastLeq(nums, j, k, upper - nums[i]);
                count += k - j + 1;
                // System.out.printf("i = %d, j = %d, k = %d\n", i, j, k);
            } else if (j == i + 1 && j < nums.length && nums[i] < nums[j] && nums[i] + nums[j] > upper) {
                break;
            }
            i++;
        }
        return count;
    }
    private int firstGeq(int[] arr, int l, int r, int v) {
        if (arr[l] >= v) return l;
        while (r - l > 1) {
            int m = (l + r) / 2;
            if (arr[m] < v) {
                l = m;
            } else {
                r = m;
            }
        }
        return r;
    }
    private int lastLeq(int[] arr, int l, int r, int v) {
        if (arr[r] <= v) return r;
        while (r - l > 1) {
            int m = (l + r) / 2;
            if (arr[m] <= v) {
                l = m;
            } else {
                r = m;
            }
        }
        return l;
    }
}
