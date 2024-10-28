class Solution {
    public int longestSquareStreak(int[] nums) {
        HashSet<Integer> hs = new HashSet();
        for (int n : nums) {
            hs.add(n);
        }
        // Note nums[i] is at least 2.
        // 2 4 16 256 65536, next will be > 10^5
        Arrays.sort(nums);
        // System.out.println("Sorted array: " + Arrays.toString(nums));
        int maxCount = 0;
        for (int n : nums) {
            long b = n;
            int count = 0;
            while (hs.contains((int)b)) {
                count++;
                if (count > maxCount) maxCount = count;
                b *= b;
                if (b > nums[nums.length - 1]) break;
            }
        }
        return maxCount > 1 ? maxCount : -1;
    }
}
