class Solution {
    public int lengthOfLIS(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        int[] lis = new int[nums.length]; // Max possible length is nums.length
        lis[0] = nums[0];
        int length = 1; // Maintains current max LIS length
        for (int i = 1; i < nums.length; i++) {
            int n = nums[i];
            if (n > lis[length-1]) {
                // Increase LIS length by adding the new number
                lis[length++] = n;
            } else {
                // n is smaller than or equal to the last element in lis,
                // which means we can potentially reduce one of the existing elements in lis,
                // giving us more chance to have longer sequence.

                // Find where n fits in the lis array,
                // if n does end up in the final longest sequence, this is where it'll be.
                int j = binarySearch(lis, 0, length, n);
                // It's ok to overwrite the value of lis[j] below,
                // because here we don't change the length variable,
                // which means the length of the previously found longest sequence is not lost.
                lis[j] = n;
            }
        }
        return length;
    }
    // Find the leftmost index k in such that arr[k-1] < n,
    // which is equivalent to finding the leftmost index m such that arr[m] >= n.
    private int binarySearch(int[] arr, int l, int r, int n) {
        if (arr[l] >= n) return l;
        while (r - l > 1) {
            int m = (l + r) / 2;
            if (arr[m] < n) {
                l = m; // arr[l] always < n
            } else {
                r = m; // arr[r] always >= n
            }
        }
        // The while loop exists when r is at most l+1.
        // So arr[l+1] must >= n, while arr[l] < n.
        return l+1;
    }
}
