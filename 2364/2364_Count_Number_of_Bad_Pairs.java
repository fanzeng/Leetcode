class Solution {
    public long countBadPairs(int[] nums) {
        int n = nums.length;
        int[] diff = new int[n]; // Difference between value and position
        HashMap<Integer, Integer> h = new HashMap<>();
        for (int i = 0; i < n; i++) {
            diff[i] = nums[i] - i;
            h.put(diff[i], h.getOrDefault(diff[i], 0) + 1);
        }
        long good = 0;
        for (Map.Entry<Integer, Integer> e : h.entrySet()) {
            long v = (long)e.getValue();
            good += v*(v-1) / 2;
        }
        return (long)n*((long)n-1)/2 - good;
    }
}
