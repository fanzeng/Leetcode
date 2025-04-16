class Solution {
    public long countGood(int[] nums, int k) {
        HashMap<Integer, Integer> m = new HashMap<>();
        long res = 0;
        int same = 0;
        int j = -1;
        for (int i = 0; i < nums.length; i++) {
            while (same < k && j + 1 < nums.length) {
                ++j;
                same += m.getOrDefault(nums[j], 0);
                m.put(nums[j], m.getOrDefault(nums[j], 0) + 1);
            }
            if (same >= k) res += nums.length-j;
            m.put(nums[i], m.get(nums[i])-1);
            same -= m.get(nums[i]);
        }
        return res;
    }
}
