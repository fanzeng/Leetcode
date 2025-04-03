class Solution {
    public long maximumTripletValue(int[] nums) {
        int n = nums.length;
        int[] maxFromStart = new int[n];
        int[] maxFromEnd = new int[n];
        int m = -1;
        for (int i = 0; i < n; i++) {
            if (nums[i] > m) m = nums[i];
            maxFromStart[i] = m;
        }
        m = -1;
        for (int i = n-1; i > -1; i--) {
            if (nums[i] > m) m = nums[i];
            maxFromEnd[i] = m;
        }
        long res = 0;
        for (int j = 1; j < n-1; j++) {
            int ms = maxFromStart[j-1];
            int me = maxFromEnd[j+1];
            if (ms < 0 && me < 0 && nums[j] < 0) continue;
            res = Math.max(res, (ms - nums[j])*(long)me);
        }
        return res;
    }
}
